from rest_framework import serializers
from .models import *

class MotoSerializer(serializers.ModelSerializer):
    motoparts = serializers.StringRelatedField(many=True)  

    class Meta:
        model = Moto
        fields = '__all__'
        many = True

class PartsMotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartsMoto
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        modle = User
        fields = '__all__'
