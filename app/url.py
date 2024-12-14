from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MotoViewset, PartsMotoViewset, UserViewset

router = DefaultRouter()
router.register(r'motos', MotoViewset)
router.register(r'partsmoto', PartsMotoViewset)
router.register(r'users', UserViewset)

urlpatterns = [
    path('api/', include(router.urls)),
]
