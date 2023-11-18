import uuid
from django.db import models
from apps.vendors.models import Vendor
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import Avg, F


class Status(models.TextChoices):
    PENDING = "pending"
    COMPLETED = "completed"
    Canceled = "canceled"


class PO(models.Model):

    po_number = models.UUIDField(default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,
                               related_name='vendor_po')
    order_date = models.DateTimeField()
    expected_delivery_date = models.DateTimeField()
    actual_delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(choices=Status.choices, max_length=10)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

    class Meta:
        db_table = "purchase_orders"
        verbose_name_plural = "Purchase Orders"
        indexes = [
            models.Index(fields=['po_number']),
        ]

    def __str__(self):
        return f"{str(self.po_number)} | {str(self.vendor.name)}"


@receiver(pre_save, sender=PO)
def cache_previous_data(sender, instance, *args, **kwargs):
    status = None
    acknowledgment_date = None
    if instance.id:
        obj = PO.objects.get(pk=instance.id)
        if obj:
            status = obj.status
            acknowledgment_date = obj.acknowledgment_date
    instance.__previous_status = status
    instance.__previous_acknowledgment_date = acknowledgment_date


@receiver(post_save, sender=PO)
def po_matrix_calculation(sender, instance, created, **kwargs):
    fields_to_update = {}
    if not created and not instance.status == instance.__previous_status:
        query = PO.objects.filter(
            vendor=instance.vendor)
        query_completed = query.filter(status=Status.COMPLETED)
        query_completed_count = query_completed.count()
        if instance.status == Status.COMPLETED:
            on_time_delivery = query_completed.filter(actual_delivery_date__lte=F('expected_delivery_date')).count()/query_completed_count
            quality_rating = query_completed.filter(quality_rating__isnull=False).aggregate(
                Avg('quality_rating'))
            fields_to_update["on_time_delivery_rate"] = on_time_delivery
            fields_to_update["quality_rating_avg"] = quality_rating.get("quality_rating__avg")
        fulfillment_rate = query_completed_count/query.count()
        fields_to_update["fulfillment_rate"] = fulfillment_rate

    if instance.acknowledgment_date and not instance.__previous_acknowledgment_date == instance.acknowledgment_date:
        average_response_time = PO.objects.filter(
            vendor=instance.vendor, acknowledgment_date__isnull=False).aggregate(
                avg_res=Avg(F('acknowledgment_date') - F('issue_date')))
        fields_to_update["average_response_time"] = average_response_time.get("avg_res").days
    if fields_to_update:
        Vendor.objects.select_for_update().filter(id=instance.vendor.id).update(**fields_to_update)