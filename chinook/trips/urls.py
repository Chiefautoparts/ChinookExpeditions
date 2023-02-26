from django.urls import path
from . import views

app_name = 'trips'

urlpatterns = [
    path('/all_trips', views.river_list, name='river_list')
]