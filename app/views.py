from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

# Create your views here.

def home(request):
    context={}
    return render(request,'home.html',context)

def detail(request):
    if request.user.is_authenticated:
        client = request.user.client
        ordre,created = Ordre.objects.get_or_create(client = client,complete=False)
        items = ordre.article_commande_set.all() 
        #items = Article_commande.objects.all()
        print(items)
        get_prix_quantite = ordre.get_prix_quantite
    else:
        items = []
        ordre = {'get_prix_total':0 , 'get_prix_quantite':0}
        get_prix_quantite = ordre['get_prix_quantite']
    produit = Produit.objects.all()
    context={
        "liste_produit":produit,
        "get_prix_quantite":get_prix_quantite
    }
    return render(request,'detail.html',context)


def panier(request):
    if request.user.is_authenticated:
        client = request.user.client
        ordre,created = Ordre.objects.get_or_create(client = client,complete=False)
        items = ordre.article_commande_set.all()
        #items = Article_commande.objects.all()
        print(items)
        get_prix_quantite = ordre.get_prix_quantite
    else:
        items = []
        ordre = {'get_prix_total':0 , 'get_prix_quantite':0}
        get_prix_quantite = ordre['get_prix_quantite']
    
    context= {
        "items": items,
        "ordre":ordre,
        "get_prix_quantite":get_prix_quantite
    }

    return render(request,'second-detail.html',context)

def paniere(request):
    context={}
    return render(request,'second-detail.html',context)


def checkout(request):
    if request.user.is_authenticated:
        client = request.user.client
        ordre,created = Ordre.objects.get_or_create(client = client,complete=False)
        items = ordre.article_commande_set.all() 
        #items = Article_commande.objects.all()
        print(items)
        get_prix_quantite = ordre.get_prix_quantite
    else:
        items = []
        ordre = {'get_prix_total':0 , 'get_prix_quantite':0}
        get_prix_quantite = ordre['get_prix_quantite']
    
    context= {
        "items": items,
        "ordre":ordre,
        "get_prix_quantite":get_prix_quantite
    }
    return render(request,'checkout.html',context)


def updateItem(request):
    data = json.loads(request.body)
    produitId = data['produit']
    action = data['action']
    print("produit_Id:",produitId)
    print("action:",action)

    client = request.user.client
    produit = Produit.objects.get(id=produitId)
    ordre,created = Ordre.objects.get_or_create(client=client, complete=False)
    article_commande,created = Article_commande.objects.get_or_create(ordre=ordre, Produit=produit)
    print("*****")
    print(article_commande)
    print("*****")

    if action == 'add':
        article_commande.quantite = (article_commande.quantite+1)
    elif action == 'remove':
        article_commande.quantite = (article_commande.quantite-1)
    article_commande.save()

    if article_commande.quantite <= 0:
        article_commande.delete()
        
    return JsonResponse("Items was added", safe=False)