import graphene
from playersapp.models import Player
from .types import *
from .resolvers import *

class PlayerQueries(graphene.ObjectType):
    all_players = graphene.List(PlayerType)
    player = graphene.Field(PlayerType, id=graphene.ID())

    def resolve_all_players(cls, info):
        return all_players()
    
    def resolve_player(cls, info, id):
        return player(id)