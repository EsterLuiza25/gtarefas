from django.db import models

STATUS_CHOICES = (
    ('Pendente', 'Pendente'),
    ('Em Andamento', 'Em Andamento'),
    ('Concluída', 'Concluída'),
)

PRIORIDADE_CHOICES = (
    ('Baixa', 'Baixa'),
    ('Média', 'Média'),
    ('Alta', 'Alta'),
)


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    titulo = models.CharField(max_length=150)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pendente'
    )
    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default='Média'
    )
    data_limite = models.DateField(null=True, blank=True)

    # (FK)
    projeto = models.ForeignKey(
        Projeto,
        related_name='tarefas',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.titulo