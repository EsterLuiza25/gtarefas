from rest_framework.routers import DefaultRouter
from .views import ProjetoViewSet, TarefaViewSet

router = DefaultRouter()

router.register(r'projetos', ProjetoViewSet)
router.register(r'tarefas', TarefaViewSet)

urlpatterns = router.urls