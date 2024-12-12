from .views import * 
from rest_framework.routers import DefaultRouter
from django.urls import path

router= DefaultRouter
router.register(r'motos', MotoViewSet)
router.register(r'partsmoto', PartsMotoView)
router.register(r'users', UserView)

urlpatterns = router.urls