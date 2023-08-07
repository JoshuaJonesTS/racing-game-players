from graphene_django import DjangoObjectType
from playersapp.models import Player
import graphene
from graphene_federation import key, shareable, requires, extend, external, provides
from .resolvers import player

@extend("id")
class VehicleType(graphene.ObjectType):
    id = external(graphene.UUID(required=True))
    players = graphene.List(lambda: PlayerType)

    def resolve_players(self, info, *args, **kwargs):
        # Get player of a given vehicle
        return Player.objects.filter(vehicle=self.id)

@key("id")
class PlayerType(DjangoObjectType):

    vehicle = graphene.Field(VehicleType)

    class Meta:
        model = Player
        fields = ("__all__")

    def resolve_vehicle(self, info):
        return VehicleType(id=self.vehicle)

    def _resolve_reference(self, info):
        return Player.objects.get(id=id)