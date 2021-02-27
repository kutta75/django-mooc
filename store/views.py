# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Album,Artist,Contact,Booking

def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    context={ 'albums':albums}
    return render(request,'store/index.html',context)

def listing(request):
    albums= Album.objects.filter(available=True)
    context = {
            'albums' : albums
            }
    return render(request,'store/listing.html',context)

def detail(request, album_id):
    album=Album.objects.get(pk=album_id)
    artists = [artist.name for artist in album.artists.all()]
    artists_name= " ".join(artists) 
    context = { 
            'album_title' : album.title,
            'artists_name' : artists_name,
            'album_id' : album.id,
            'thumbnail' : album.picture
            }
    return render(request,'store/detail.html',context)

def search(request):
    query= request.GET.get('query')
    albums= Album.objects.all()
    print("type of albums = ",type(albums))
    if not query:
        albums = Album.objects.all()
    else:
        albums= Album.objects.filter(title__icontains=query)
    if not albums.exists(): 
        albums= Album.objects.filter(artists__name__icontains = query )
    if not albums.exists():
        message="nous n'avons trouvé aucun résultat"
    else:
        albums=["< {}</li>".format(album.title) for album in albums ]
        message = """
                nous avons trouvé les albums correspondant à votre requete: les voici : <ul>
                {}
                </ul>
                """.format("</li><li>".join(albums))
    title="Résultat pour la recherche %s" %query
    context = {
            'albums' : albums,
            'title' : title
            }
    return render(request,'store/search.html',context)
