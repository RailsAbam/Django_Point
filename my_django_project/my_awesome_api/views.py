from django.shortcuts import render
from rest_framework import serializers, viewsets
from my_awesome_api.models import Person,Species
from my_awesome_api .serializers import PersonSerializer, SpeciesSerializer

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer 


