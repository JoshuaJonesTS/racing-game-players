from playersapp.models import Player

def all_players():
    return Player.objects.all()

def player(id):
    return Player.objects.get(id=id)