from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Bonjour le monde, Je vous salue depuis le Cabinet Djetaba")
