from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from cadastro.models import Livros
from cadastro.models import Alunos


class Locacao(models.Model):
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    data_locacao = models.DateField(default=timezone.now)
    data_devolucao = models.DateField(null=True, blank=True, default=timezone.now() + timezone.timedelta(days=14))
    devolvido = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Efetuar Locação'
        verbose_name_plural = 'Efetuar Locação'

    def __str__(self):
        return f"{self.livro.titulo} - {self.aluno.nome}"

    def clean(self):
        # Verificar se a Data de Devolução é menor que a de Locação (Não pode)
        if self.data_devolucao and self.data_devolucao < self.data_locacao:
            raise ValidationError('A data de devolução não pode ser anterior à data de locação.')

        # Verificar se o livro está disponível para locação (qtd_disponivel > 0)
        if self.livro.qtd_disponivel == 0:
            raise ValidationError('Não há exemplares disponíveis do livro selecionado para locação.')

        # Baixa de 1 item no estoque de livros ao locar
        self.livro.qtd_disponivel -= 1
        self.livro.save()
