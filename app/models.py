from django.db import models

class Moto(models.Model):
    MOTO_TYPE_CHOICES = [
        ('sport', 'Sport'),
        ('bigtrail', 'Bigtrail'),
        ('naked', 'Naked'),
        ('custom', 'Custom'),
    ]
    name = models.CharField(max_length=100)
    moto_type = models.CharField(max_length=50, choices=MOTO_TYPE_CHOICES, default='sport')

    def __str__(self):
        return f"{self.name} ({self.get_moto_type_display()})"


class PartsMoto(models.Model):
    PART_TYPE_CHOICES = [
        ('sport', 'Sport'),
        ('bigtrail', 'Bigtrail'),
        ('naked', 'Naked'),
        ('custom', 'Custom'),
    ]
    name = models.CharField(max_length=100, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    src = models.CharField(max_length=1000, blank=True)
    part_type = models.CharField(max_length=50, choices=PART_TYPE_CHOICES)
    moto_fk = models.ForeignKey(Moto, related_name='motoparts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.get_part_type_display()})"


class User(models.Model):
    email = models.CharField(max_length=200,unique=True)
    cpf = models.CharField(max_length=11,unique=True)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.email