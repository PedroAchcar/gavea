from django.db import models


class Transacao(models.Model):
    ticker = models.CharField(max_length=10)
    preco_compra = models.FloatField()
    quantidade = models.IntegerField()
    total = models.FloatField(blank=True, null=True)
    posicao_atual = models.FloatField(blank=True, null=True)
    data_compra = models.DateTimeField(auto_now_add=True)
