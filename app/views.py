from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError


class MotoViewset(ModelViewSet):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer

class PartsMotoViewset(ModelViewSet):
    queryset = PartsMoto.objects.all()
    serializer_class = PartsMotoSerializer

    def get_queryset(self):
        moto_type = self.request.query_params.get('moto_type')
        if moto_type:
            return self.queryset.filter(part_type=moto_type)
        return self.queryset

    def perform_create(self, serializer):
        
        part_type = serializer.validated_data.get('part_type')
        moto_fk = serializer.validated_data.get('moto_fk')
        if moto_fk.moto_type != part_type:
            raise ValidationError("O tipo da peça não é compatível com o tipo da moto.")
        serializer.save()

class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer