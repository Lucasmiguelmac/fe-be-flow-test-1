import strawberry
from typing import List
from strawberry_django import mutations

from fruits.types import Fruit, FruitInput, Color, ColorInput


@strawberry.type
class Query:
    fruits: List[Fruit] = strawberry.django.field()
    colors: List[Color] = strawberry.django.field()

@strawberry.type
class Mutation:
    createColor: Color = mutations.create(ColorInput)
    createFruit: Fruit = mutations.create(FruitInput)

schema = strawberry.Schema(query=Query, mutation=Mutation)