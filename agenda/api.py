from rest_framework import viewsets, routers, serializers
from .models import *


myroute = routers.DefaultRouter()

class CompteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Compte
        field = ['url']