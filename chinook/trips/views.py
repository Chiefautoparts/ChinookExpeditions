from django.shortcuts import render
from .models import River

def river_list(request):
    rivers = River.objects.all()
    return render(request, 'trips/all_trips.html', {'rivers', rivers})