from django.db import models

class User(models.Model):
    favoritos = models.CharField(max_length=20)

    def __str__(self):
        return {self.favoritos}

class Cripto(models.Model):
    nome = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome