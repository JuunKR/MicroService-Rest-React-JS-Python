from django.urls import path
from .views import Members as members
from .views import Member as member
from django.conf.urls import url

urlpatterns = [
    path('/signup', members.as_view()),
    path('/login', member.as_view())
]