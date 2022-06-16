from django.urls import path
from .views import Home, Chess

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('chess/', Chess.as_view(), name="chess"),
]