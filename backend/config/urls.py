from django.contrib import admin
from django.urls import include, path
from django.conf import settings

prefix = "api"
urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{prefix}/vendors/', include('apps.vendors.urls', namespace="vendors")),
    path(f'{prefix}/purchase_orders/',
         include('apps.po.urls', namespace="purchase_orders")),
]


if settings.ENV == "L":
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
