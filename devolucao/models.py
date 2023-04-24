from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from locacao.models import Locacao

class Devolucao(models.Model):
    locacao = models.OneToOneField(Locacao, on_delete=models.CASCADE)
    data_devolucao = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Efetuar Devolução'
        verbose_name_plural = 'Efetuar Devolução'

    def __str__(self):
        return f"Devolução da locação {self.locacao.id} - {self.locacao.livro.titulo} - {self.locacao.aluno.nome}"

    def save(self, *args, **kwargs):
        self.locacao.devolvido = True
        self.locacao.save()
        self.locacao.livro.qtd_disponivel += 1
        self.locacao.livro.save()
        super().save(*args, **kwargs)
