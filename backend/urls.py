from rest_framework.routers import DefaultRouter

from .views import MovieApiView

router = DefaultRouter()
router.register('movies', MovieApiView)

urlpatterns = router.urls