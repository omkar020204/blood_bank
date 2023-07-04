from django.contrib import admin
from django.urls import path,include
from . import views
app_name='buy'
urlpatterns = [
    path('',views.index,name="home"),
    path('success/',views.success,name="success"),
    path('fail/',views.fail,name="fail"),
]
