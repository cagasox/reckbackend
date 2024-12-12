from django.db import models

class Moto(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PartsMoto(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    src = models.CharField(max_length=1000,blank=True)
    part_type = models.CharField(max_length=100)  
    moto_fk = models.ForeignKey(Moto, related_name='motoparts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class User(models.Model):
    email = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11) 
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.email
