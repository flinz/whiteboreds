from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from whbs_backend import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'scores', views.ScoreViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^', include(router.urls))
]
