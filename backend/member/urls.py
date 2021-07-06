from member import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    url(r'^register', views.members),
    url(r'^list', views.members),
    url(r'^login', views.login),
    path('delete/<slug:pk>', views.member),
    url(r'^modify', views.member_modify),
]