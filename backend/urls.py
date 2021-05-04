from rest_framework.routers import DefaultRouter

from .views import MovieApiView, GenreApiView

router = DefaultRouter()
router.register('movies', MovieApiView)
router.register('genres', GenreApiView)

urlpatterns = router.urls