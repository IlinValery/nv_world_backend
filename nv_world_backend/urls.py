from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('', include('nv_profile.urls')),
    path('', include('nv_service.urls')),
]
