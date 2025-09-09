from django.db import models

class Band(models.Model):
    # Ensuite, nous ajoutons un attribut de classe à notre classe name. 
    # À cet attribut, nous attribuons unCharField, qui est l'abréviation de Character Field. 
    # Il s'agira d'un champ qui stocke des données de type caractère/texte/chaîne, 
    # ce qui est le type de données approprié pour un nom.
    name = models.fields.CharField(max_length=100)


class Listing(models.Model):
    title = models.fields.CharField(max_length=100)

