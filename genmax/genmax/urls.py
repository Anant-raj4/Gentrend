from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', include('base.urls'))
]
