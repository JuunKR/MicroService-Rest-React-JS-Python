from common.views import Connection
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('connection', Connection.as_view()),
    path('board', include('board.urls')),
    path('member', include('member.urls')),
    # url(r'^member', Auth.as_view()),
    # path('admin/', admin.site.urls),
]