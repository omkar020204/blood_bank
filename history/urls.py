from django.contrib import admin
from django.urls import path,include
from . import views
app_name='history'
urlpatterns = [
    path('',views.index,name="home"),
    path('result/',views.result,name="result"),
]
