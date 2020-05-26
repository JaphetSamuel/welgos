from rest_framework import viewsets, routers, serializers
from .models import *
from django.urls import path, include


myroute = routers.DefaultRouter()


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class OrganisationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Organisation
        fields = ['url', 'user', 'info', 'img_url', 'banner_url', 'siteweb', 'contact', 'facebook', 'suiveur']


class EventSerailizer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Event
        fields = ['theme', 'organisateur', 'lieu', 'horodage', 'affiche_url', 'reservations']


class UserVS(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OrganisationVS(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer


class EventVS(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerailizer


myroute.register('user', UserVS),
myroute.register('organisation', OrganisationVS)
myroute.register('event', EventVS)

urlpatterns = [
    path('', include(myroute.urls)),
]
