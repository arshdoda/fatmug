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

