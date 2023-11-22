from django.shortcuts import render
from rest_framework import generics
from apps.po.models import PO
from apps.po.serializers import PoSerializer, PoAcknowledgeSerializer
from django.db.models.query import QuerySet
from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from apps.vendors.models import Vendor
from django.db.models import Avg, F
from apps.po.models import Status


class POListCreateAPIView(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = PO.objects.all().order_by("id")
    serializer_class = PoSerializer
    pagination_class = PageNumberPagination


class PORetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'put', 'delete']
    queryset = QuerySet(PO)
    serializer_class = PoSerializer
    lookup_field = 'pk'


class POAcknowledgeAPIView(generics.UpdateAPIView):
    http_method_names = ['put']
    queryset = QuerySet(PO)
    serializer_class = PoAcknowledgeSerializer
    lookup_field = 'pk'


# This Api View should only be called while creating data using dummy_data.py.
# Since, dumm_data.py uses bulk_create which does not trigger post_save signal,
# we are calling this api 
class POMatrixAPIView(generics.GenericAPIView):
    http_method_names = ['get']
    serializer_class = None

    def get(self, request, *args, **kwargs):
        created = False
        for v in Vendor.objects.all():
            instance = PO.objects.filter(vendor=v).first()

            if instance:
                fields_to_update = {}
                if not created:
                    query = PO.objects.filter(
                        vendor=instance.vendor)
                    query_completed = query.filter(status=Status.COMPLETED)
                    query_completed_count = query_completed.count()
                    if query_completed_count > 0:
                        on_time_delivery = query_completed.filter(actual_delivery_date__lte=F(
                            'expected_delivery_date')).count()/query_completed_count
                        quality_rating = query_completed.filter(quality_rating__isnull=False).aggregate(
                            Avg('quality_rating'))
                        fields_to_update["on_time_delivery_rate"] = on_time_delivery
                        fields_to_update["quality_rating_avg"] = quality_rating.get(
                            "quality_rating__avg")
                    fulfillment_rate = query_completed_count/query.count()
                    fields_to_update["fulfillment_rate"] = fulfillment_rate

                average_response_time = PO.objects.filter(
                    vendor=instance.vendor, acknowledgment_date__isnull=False).aggregate(
                        avg_res=Avg(F('acknowledgment_date') - F('issue_date')))
                fields_to_update["average_response_time"] = average_response_time.get(
                    "avg_res").days
                if fields_to_update:
                    Vendor.objects.select_for_update().filter(
                        id=instance.vendor.id).update(**fields_to_update)
        return Response(
            {
                "message": "Success"
            },
            status=200
        )
