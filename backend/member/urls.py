from member import views
from django.conf.urls import url

urlpatterns = [
    url(r'^register', views.members),
    url(r'^list', views.members),
    url(r'^login', views.member),
    url(r'^modify', views.member)

]