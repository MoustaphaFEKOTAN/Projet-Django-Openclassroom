from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
def hello(request):
     bands = Band.objects.all()
     
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')