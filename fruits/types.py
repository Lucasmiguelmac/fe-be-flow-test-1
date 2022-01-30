import strawberry
from enum import Enum
from strawberry.django import auto
from typing import List
import strawberry_django

from fruits import models

@strawberry.enum
class ColorName(Enum):
    RED     = "Rojo"
    YELLOW  = "Amarillo"
    BLUE    = "Azul"
    ORANGE  = "Naranja"
    PURPLE  = "Violeta"
    GREEN   = "Verde"

@strawberry.django.type(models.Fruit)
class Fruit:
    id: auto
    name: auto
    color: 'Color'
    amount: auto

@strawberry.django.type(models.Color)
class Color:
    id: auto
    name: auto
    fruits: auto

@strawberry_django.input(models.Color)
class ColorInput:
    id: auto
    name: auto
    fruits: auto