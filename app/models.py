from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nom = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField(max_length=200)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.nom

    @property
    def  imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url
        
class Ordre(models.Model):
    client = models.ForeignKey(Client,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordre = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=True)
    transaction_id = models.CharField(max_length=200, null = True)

    def __str__(self):
        return str(self.id)

    @property
    def get_prix_total(self):
        article_commande = self.article_commande_set.all()
        total = sum([article.totale for article in article_commande])
        return total

    @property
    def get_prix_quantite(self):
        article_commande = self.article_commande_set.all()
        quantite = sum([article.quantite for article in article_commande])
        return quantite

class Article_commande(models.Model):
    Produit = models.ForeignKey(Produit,on_delete=models.SET_NULL,blank=True,null=True)
    ordre = models.ForeignKey(Ordre,on_delete=models.SET_NULL,blank=True,null=True)
    quantite = models.IntegerField(default=0,blank=True,null=True)
    date_ajouter = models.DateTimeField(auto_now_add=True)
    
    @property
    def totale(self):
        total = self.Produit.prix * self.quantite
        return total

class Adresse_de_livraison(models.Model):
    client = models.ForeignKey(Client,on_delete=models.SET_NULL,blank=True,null=True)
    ordre = models.ForeignKey(Ordre,on_delete=models.SET_NULL,blank=True,null=True)
    adresse = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    Etat = models.CharField(max_length=200,null=True)
    code = models.CharField(max_length=200,null=True)
    date_ajouter = models.DateTimeField(auto_now_add=True)

    def __srt__(self):
        return self.adresse


