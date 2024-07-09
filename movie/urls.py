from rest_framework import routers

from movie import views

app_name = 'movie'

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'movies', views.MovieViewSet, basename='movies')

urlpatterns = router.urls
