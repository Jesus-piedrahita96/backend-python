from rest_framework import routers

from .api import TodoViewSet, MenuViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('api/todos', TodoViewSet, 'todos')
router.register('api/menu', MenuViewSet, 'menu')
router.register('api/post', PostViewSet, 'post')

urlpatterns = router.urls