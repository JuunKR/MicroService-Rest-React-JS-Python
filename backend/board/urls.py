from django.urls import path
from .views import Boards as board

urlpatterns = [

    path('/register', board.as_view())
]