import datetime
from django.db import models


# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.nom


class Commande(models.Model):
    date = models.DateField(datetime.date.today)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=False)


class Produit(models.Model):
    nom = models.CharField(max_length=32, null=False)


class Possede(models.Model):
    quantite = models.IntegerField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, null=True)
