
from django.conf.urls import url
from nv_profile.views import LoginView, LogoutView

urlpatterns = [
    url(r'^api/auth/login', LoginView.as_view()),
]
