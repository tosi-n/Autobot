from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('nlp_bot', views.BitronView),
urlpatterns = [
    path('api/', include(router.urls)),
    path('bitron/', views.binatron),
]