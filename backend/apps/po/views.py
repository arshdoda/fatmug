from django.shortcuts import render
from rest_framework import generics
from apps.po.models import PO
from apps.po.serializers import PoSerializer, PoAcknowledgeSerializer
from django.db.models.query import QuerySet

class POListCreateAPIView(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = PO.objects.all()
    serializer_class = PoSerializer



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
