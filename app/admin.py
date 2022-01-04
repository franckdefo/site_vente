from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Produit)
admin.site.register(Ordre)
admin.site.register(Article_commande)
admin.site.register(Adresse_de_livraison)

