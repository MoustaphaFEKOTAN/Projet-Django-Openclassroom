from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band,Listing

def hello(request):
    bands = Band.objects.all()
    return render(request,
    'bands/hello.html',
    {'bands': bands})


def articles(request):
    articles = Listing.objects.all()
    return render(request,
    'listings/article.html',
    {'articles': articles})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')