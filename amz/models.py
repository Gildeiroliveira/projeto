from django.db import models

# Create your models here.
class Produto (models.Model):
    codigo_pro = models.CharField(max_length=100, primary_key=True, blank=False, null=False)
    nome = models.TextField(max_length=50)
    preco = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    categoria = models.TextField(max_length=12, default='Sem mais detalhes')