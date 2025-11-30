from rest_framework import serializers
from .models import Projeto, Tarefa

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['id', 'nome', 'descricao', 'data_criacao']
        read_only_fields = ['data_criacao']

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = [
            'id',
            'titulo',
            'status',
            'prioridade',
            'data_limite',
            'projeto' 
        ]