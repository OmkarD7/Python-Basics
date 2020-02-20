from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to Music App!</h1>")

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album Id: "+ str(album_id))
