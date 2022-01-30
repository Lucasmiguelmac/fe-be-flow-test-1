import strawberry
from enum import Enum
from strawberry.django import auto
from typing import List
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

@strawberry.django.type(models.Color)
class Color:
    id: auto
    name: ColorName
    fruits: List[Fruit]