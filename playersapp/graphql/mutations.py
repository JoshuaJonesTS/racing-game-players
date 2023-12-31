import graphene
from .types import PlayerType
from playersapp.models import Player

class CreatePlayer(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        vehicle = graphene.UUID(required=True)  # graphene federation
       
    player = graphene.Field(PlayerType)

    @classmethod
    def mutate(cls, root, info, **kwargs):    
        new_player = Player.objects.create(
            name = kwargs.get('name'),
            vehicle = kwargs.get('vehicle') # graphene federation
        )
        return CreatePlayer(player=new_player)
    
class EditPlayer(graphene.Mutation):
    class Arguments:
        id = graphene.UUID(required=True)
        name = graphene.String()
        vehicle = graphene.UUID(required=True) # graphene federation

    player = graphene.Field(PlayerType)

    @classmethod
    def mutate(cls, root, info, **kwargs):     
        try:   
            new_player = Player.objects.get(pk=kwargs.get('id'))
        except Player.DoesNotExist:
            raise Exception('Player does not exist')

        if 'name' in kwargs:
            new_player.name=kwargs.get('name') 

        if 'vehicle' in kwargs:
            new_player.vehicle=kwargs.get('vehicle') # graphene federation

        new_player.save()

        return EditPlayer(player=new_player)
    
class PlayerMutations(graphene.ObjectType):
    create_player = CreatePlayer.Field()
    edit_player = EditPlayer.Field()
