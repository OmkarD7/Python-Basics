from django.shortcuts import render
from django.http  import HttpResponse
from .models import Album
from django.template import loader
from django.http import Http404


# Create your views here.
def home(request):
    html  = ""
    allAlbums = Album.objects.all() 
    #creating dictionary to use it inside template
    container = {
        'allAlbums': allAlbums,
    }
    print(allAlbums)
    template  = loader.get_template('music/index.html')
    return HttpResponse(template.render(container, request))
    """ 
    for album in allAlbums:
        print(album)
        #<a href="#">album title</a>
        html += "<a href=" + str(album.id) + ">" + str(album.album_title) + "</a> <br>"
    return HttpResponse("<h1>Welcome to Music App!</h1><br>" + html)
 """
def detail(request, album_id):
    template  = loader.get_template('music/detail.html')
    try:
        album = Album.objects.get(pk=album_id)
        print(album)
        container = {
            "album":album
        }
    except Album.DoesNotExist:
        raise Http404("Album Does Not Exist For Id: " + str(album_id))    
    return HttpResponse(template.render(container,request))