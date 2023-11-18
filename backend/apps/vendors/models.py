from django.db import models
import uuid 


class Vendor(models.Model):

    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.UUIDField(default = uuid.uuid4, editable = False) 
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    class Meta:
        db_table = "vendors"
        verbose_name_plural = "Vendor Details"
        indexes = [
            models.Index(fields=['vendor_code']),
        ]

    def __str__(self):
        return f"{str(self.id)} | {str(self.name)}"




class HistoricPerformance(models.Model):

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,
                             related_name='vendor_hp')
    edited_on = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    class Meta:
        db_table = "vendors_historic_performance"
        verbose_name_plural = "Vendor Historic Peformance"

    def __str__(self):
        return f"{str(self.vendor.id)} | {str(self.vendor.name)}"