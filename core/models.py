from django.db import models

class Cripto(models.Model):
    nome    = models.CharField(max_length=100)
    simbolo = models.CharField(max_length=20)
    preco   = models.FloatField()

    def __str__(self):
        return self.nome


class Favorito(models.Model):
    nome    = models.CharField(max_length=100, unique=True)
    simbolo = models.CharField(max_length=20)
    preco   = models.FloatField()

    def __str__(self):
        return self.nome