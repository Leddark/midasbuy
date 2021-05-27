from django.urls import path
from . views import index , home , verification
from django.conf.urls import url

urlpatterns = [
    path('', index , name="index"),
    path('home', home , name="home"),
    path('verification', verification , name="verification"),

    


]
