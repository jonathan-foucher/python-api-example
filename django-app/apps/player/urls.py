from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from apps.player import views

router = DefaultRouter()
router.register(r'players', views.PlayerViewSet)

urlpatterns = [re_path(r'^', include(router.urls))]
