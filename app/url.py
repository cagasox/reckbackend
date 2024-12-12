from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Configuração do roteador
router = DefaultRouter()
router.register(r'motos', MotoView)
router.register(r'partsmoto', PartsMotoView)
router.register(r'users', UserView)

# URLs da API
urlpatterns = [
    path('api/', include(router.urls)),
]
