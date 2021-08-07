import graphene
from graphene_django import DjangoObjectType

from coffee.models import Coffee

class CoffeeType(DjangoObjectType):
    class Meta:
        model = Coffee

class Query(graphene.ObjectType):
    coffees = graphene.List(CoffeeType)

    def resolve_coffees(self, info, **kwargs):
        return Coffee.objects.all()

class CreateCoffee(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()

    class Arguments:
        name = graphene.String()
        description = graphene.String()

    def mutate(self, info, name, description):
        coffee = Coffee(name=name, description=description)
        coffee.save()

        return CreateCoffee(
            id=coffee.id,
            name=coffee.name,
            description=coffee.description,
        )

class Mutation(graphene.ObjectType):
    create_coffee = CreateCoffee.Field()