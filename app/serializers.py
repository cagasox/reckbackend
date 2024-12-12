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
        fields = '__all__'
        many = True

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        many = True