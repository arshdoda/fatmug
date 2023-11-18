from django.urls import path

from .views import *

app_name = 'vendors'

urlpatterns = [
    path('', VendorListCreateAPIView.as_view(), name='list-create-vendors'),
    path('<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(),
         name='retrieve-update-delete-vendor'),
    path('<int:pk>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
]
