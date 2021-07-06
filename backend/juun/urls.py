from common.views import Connection
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('connection', Connection.as_view()), # 하나만 있을 때
    url(r'^api/post/', include('board.urls')),
    url(r'^api/member/', include('member.urls')),
    url(r'^adm/member/', include('member.urls')),

]


'''
CBV 방식
from common.views.py import Connection
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
router = routers.DefaultRouter()
urlpatterns = [
    path('/connection', Connection.as_view()),
    path('/api/post', include('board.urls')),
    path('/api/member', include('member.urls')),
    path('/adm/member', include('member.urls')),
    # url(r'^member', Auth.as_view()),
    # path('admin/', admin.site.urls),
]'''