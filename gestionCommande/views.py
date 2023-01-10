from django.shortcuts import render, redirect
from gestionCommande.models import Commande, Produit, Possede
from forms import frmCommande


# Create your views here.

def afficher_index(request):
    liste_produits = Produit.objects.all()
    liste_commandes = Commande.objects.all()
    quantite_produit_commande = Possede.objects.all()
    context = {"commandes": liste_commandes, "produits": liste_produits, "quantite_produits": quantite_produit_commande}
    return render(request, 'index.html', context)


def ajouter_commande(request):
    formulaire_commande = frmCommande
    liste_commandes = Commande.objects.all()
    if request.method == 'POST':
        form = frmCommande(request.POST)
        if form.is_valid():
            form.save()
            return redirect(afficher_index)
    return render(request, 'ajouter_commande.html',  {"commandes": liste_commandes, "form": formulaire_commande})
