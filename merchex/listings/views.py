from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band,Listing

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
""")


def articles(request):
    articles = Listing.objects.all()
    return HttpResponse(f"""
       
        <p>Nos articles :<p>
        <ul>
            <li>{articles[0].title}</li>
            <li>{articles[1].title}</li>
            <li>{articles[2].title}</li>
        </ul>
""")

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')