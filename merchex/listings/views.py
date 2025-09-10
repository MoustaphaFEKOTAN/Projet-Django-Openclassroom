from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band,Listing
from django.http import Http404

def band_list(request):
    bands = Band.objects.all()
    return render(request,
    'bands/band_list.html',
    {'bands': bands})

def band_detail(request, band_id):
  try:
      band = Band.objects.get(id=band_id)
  except Band.DoesNotExist:
        return render(request,
          'bands/404.html', status=404)

  return render(request,
          'bands/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def band_listing(request, band_id):
    try:
        band = Band.objects.get(id=band_id)
    except Band.DoesNotExist:
        return render(request,
          'bands/404.html', status=404)

    listings = Listing.objects.filter(band=band) # nous filtrons les annonces pour n'inclure que celles du groupe spécifié
     # nous passons à la fois les annonces et le groupe au gabarit

    return render(request,
          'bands/band_listing.html',
          {'listings': listings, 'band': band})


def articles(request):
    articles = Listing.objects.all()
    return render(request,
    'listings/article.html',
    {'articles': articles})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')