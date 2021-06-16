from django.shortcuts import render, get_object_or_404
from .models import Place

# Create your views here.
def index(request):
    places = Place.objects.all()
    context = {'places': places}
    return render(request, 'travello/homepage.html', context)

def destination(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    context = {'place': place}
    return render(request, 'travello/destination.html', context)
    