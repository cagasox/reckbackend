from django.contrib import admin
from .models import *

from django.contrib import admin
from .models import Moto, PartsMoto, User

@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(PartsMoto)
class PartsMotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'part_type', 'moto_fk')
    search_fields = ('name', 'part_type')
    list_filter = ('part_type', 'moto_fk')
    ordering = ('name',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'cpf', 'phone')
    search_fields = ('email', 'cpf')
    ordering = ('email',)

