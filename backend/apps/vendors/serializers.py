# from apps.map.models import Shapefile
from apps.vendors.models import Vendor, HistoricPerformance
from rest_framework import serializers


class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = ["name", "contact_details", "address"]
        read_only_fields = ['vendor_code']



class VendorPerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = "__all__"
