from apps.po.models import PO
from rest_framework import serializers
from django.conf import settings


class PoSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(format=settings.DATE_TIME_FORMAT)
    expected_delivery_date = serializers.DateTimeField(format=settings.DATE_TIME_FORMAT)    
    actual_delivery_date = serializers.DateTimeField(format=settings.DATE_TIME_FORMAT)    
    issue_date = serializers.DateTimeField(format=settings.DATE_TIME_FORMAT)    
    acknowledgment_date = serializers.DateTimeField(format=settings.DATE_TIME_FORMAT)    
    
    class Meta:
        model = PO
        fields = "__all__"
        read_only_fields = ['po_number']

class PoAcknowledgeSerializer(serializers.ModelSerializer):
    acknowledgment_date = serializers.DateTimeField(format=settings.DATE_TIME_FORMAT)    
    
    class Meta:
        model = PO
        fields = ["acknowledgment_date"]
