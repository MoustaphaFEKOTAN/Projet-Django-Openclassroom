from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):

    # Ensuite, nous ajoutons un attribut de classe à notre classe name. 
    # À cet attribut, nous attribuons unCharField, qui est l'abréviation de Character Field. 
    # Il s'agira d'un champ qui stocke des données de type caractère/texte/chaîne, 
    # ce qui est le type de données approprié pour un nom.

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Listing(models.Model):

    class Type(models.TextChoices):
        Records = 'Record'
        Clothing = 'clothing'
        Posters = 'Posters'
        Miscellaneous = 'Miscellaneous'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2021)] )
    type =  models.fields.CharField(choices=Type.choices, max_length=20)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL) #Clé étrangère faisant référence au modèle Band