from django.urls import path
from . import views

urlpatterns = [
    path( 'member/signup', views.member_list)
]