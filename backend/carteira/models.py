from django.db import models


class Acao(models.Model):
    codigo = models.CharField(max_length=255)
    preco = models.DecimalField()
    quantidade = models.PositiveIntegerField()
    total = models.DecimalField()
