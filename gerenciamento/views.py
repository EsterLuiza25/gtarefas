from rest_framework import viewsets
from .models import Projeto, Tarefa
from .serializers import ProjetoSerializer, TarefaSerializer

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all().order_by('nome')
    serializer_class = ProjetoSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all().order_by('data_limite')
    serializer_class = TarefaSerializer

    def get_queryset(self):
        queryset = Tarefa.objects.all()

        projeto_id = self.request.query_params.get('projeto', None)

        if projeto_id is not None:
            queryset = queryset.filter(projeto=projeto_id)

        return queryset