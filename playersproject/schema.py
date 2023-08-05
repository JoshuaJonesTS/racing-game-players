from graphene_federation import build_schema

from playersapp.graphql.schema import PlayerQueries
from playersapp.graphql.mutations import PlayerMutations

class Query(
    PlayerQueries,
):
    pass

class Mutation(
    PlayerMutations
):
    pass

schema = build_schema(query=Query, mutation=Mutation, enable_federation_2=True)