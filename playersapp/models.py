import uuid
from django.db import models
# The Vehicle model is in a separate repository. If I recall correctly, this is where graphene-federation comes into play. Either that, or Node.js
# from core.models import VehicleField 

# Create your models here.
class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=15)
    # vehicle = models.VehicleField()

    def __str__(self):
        return self.name