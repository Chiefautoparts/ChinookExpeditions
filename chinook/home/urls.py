from . import views
from django.urls import path 

app_name='home'

urlpatterns = [
    path('', views.home, name='home'),
    path('reviews', views.reviews, name='reviews'),
    path('add_review', views.add_review, name='add_review'),
    path('work', views.our_work, name='our_work'),
    path('about', views.about, name='about')
]