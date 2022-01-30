from django.db import models


class Fruit(models.Model):
    name    = models.CharField(max_length=20)
    color   = models.ForeignKey('Color', blank=True, null=True, related_name='fruits', on_delete=models.CASCADE)


class Color(models.Model):

    class ColorChoices(models.TextChoices):
        RED     = "Rojo"
        YELLOW  = "Amarillo"
        BLUE    = "Azul"
        ORANGE  = "Naranja"
        PURPLE  = "Violeta"
        GREEN   = "Verde"

    name = models.CharField(choices=ColorChoices.choices, max_length=20)