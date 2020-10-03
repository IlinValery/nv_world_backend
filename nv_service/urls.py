from nv_service.views import TestConnection
from django.conf.urls import url

urlpatterns = [
    url(r'^api/test_connection/', TestConnection.as_view()),
]
