from django.urls import path

from .views import *

app_name = 'po'

urlpatterns = [
    path('', POListCreateAPIView.as_view(), name='list-create-po'),
    path('<int:pk>/', PORetrieveUpdateDestroyAPIView.as_view(),
         name='retrieve-update-delete-po'),
    path('<int:pk>/acknowledge', POAcknowledgeAPIView.as_view(),
         name='acknowledge-po'),

    # Only required if data is generated using dummy_data.py file.
    path('calculate_matrix/', POMatrixAPIView.as_view(), name='po-matrix'),
]
