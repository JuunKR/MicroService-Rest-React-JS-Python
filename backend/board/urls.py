from django.urls import path
from .views import Boards as board

urlpatterns = [

    path('/write', board.as_view())
]