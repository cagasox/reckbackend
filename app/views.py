from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

class MotoView(ModelViewSet):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer

class PartsMotoView(ModelViewSet):
    queryset = PartsMoto.objects.all()
    serializer_class = PartsMotoSerializer

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer