from django import forms
from django.forms import ModelForm
from gestionCommande.models import *


class frmCommande(ModelForm):
    class Meta:
        model = Commande
        fields = "__all__"
