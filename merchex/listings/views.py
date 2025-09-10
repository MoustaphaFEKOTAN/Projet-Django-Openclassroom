from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band,Listing
from django.http import Http404
from listings.forms import ContactUsForm,BandForm
from django.core.mail import send_mail
from django.shortcuts import redirect

def band_list(request):
    bands = Band.objects.all()
    return render(request,
    'bands/band_list.html',
    {'bands': bands})

#   Détail de model
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





def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                #form.cleaned_data est un dict contenant les données du formulaire après qu'elles ont subi le processus de validation
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
        return redirect('contact')
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
    # ceci doit être une requête GET, donc créer un formulaire vide
          form = ContactUsForm()

    return render(request,
            'listings/contact.html',
            {'form': form})

#   Création de model
def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'bands/band_create.html',
            {'form': form})


#   Mise à jour de model
def band_update(request, band_id):
    try:
        band = Band.objects.get(id=band_id)
    except Band.DoesNotExist:
        return render(request,
                      'bands/404.html', status=404)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,
                'bands/band_update.html',
                {'form': form})

#   Suppression de model
def band_delete(request, band_id):
    try:
        band = Band.objects.get(id=band_id)
    except Band.DoesNotExist:
        return render(request,
                      'bands/404.html', status=404)

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'bands/band_delete.html',
                    {'band': band})
...


def articles(request):
    articles = Listing.objects.all()
    return render(request,
    'listings/article.html',
    {'articles': articles})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')