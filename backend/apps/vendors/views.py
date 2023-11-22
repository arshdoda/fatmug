from django.shortcuts import render
from rest_framework import generics
from apps.vendors.models import Vendor
from apps.vendors.serializers import VendorSerializer, VendorPerformanceSerializer
from django.db.models.query import QuerySet
from rest_framework.pagination import PageNumberPagination


class VendorListCreateAPIView(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = Vendor.objects.all().order_by("id")
    serializer_class = VendorSerializer
    pagination_class = PageNumberPagination


class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'put', 'delete']
    queryset = QuerySet(Vendor)
    serializer_class = VendorSerializer
    lookup_field = 'pk'


class VendorPerformanceAPIView(generics.RetrieveAPIView):
    http_method_names = ['get']
    queryset = QuerySet(Vendor)
    serializer_class = VendorPerformanceSerializer
    lookup_field = 'pk'
