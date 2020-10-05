
from django.conf.urls import url
from nv_profile.views import LoginView, LogoutView, UserView, CurrentRoomView, SkillsUsedView, SkillsAllView, \
    UpproveSkillToUser

urlpatterns = [
    url(r'^api/auth/login', LoginView.as_view()),
    url(r'^api/auth/logout', LogoutView.as_view()),
    url(r'^api/user/(?P<user_id>\d+)', UserView.as_view()),
    url(r'^api/room/by_user/(?P<user_id>\d+)', CurrentRoomView.as_view()),
    url(r'^api/skills/avail/', SkillsUsedView.as_view()),
    url(r'^api/skills/all/', SkillsAllView.as_view()),
    url(r'^api/task/complete/', UpproveSkillToUser.as_view()),
]

