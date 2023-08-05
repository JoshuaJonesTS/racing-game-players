from graphene_django import DjangoObjectType
from playersapp.models import Player
import graphene
from graphene_federation import key
from .resolvers import player

@key("id")
class PlayerType(DjangoObjectType):

    class Meta:
        model = Player
        fields = ("__all__")

    def _resolve_reference(self, info):
        return Player.objects.get(id=self.id)