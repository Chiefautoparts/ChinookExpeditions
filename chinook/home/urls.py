from . import views
from django.urls import path 

app_name='home'

urlpatterns = [
    path('', views.home, name='home'),
    #path('index', views.index, name='index')
]