from django.shortcuts import render
from rest_framework import generics
from .models import Buch, Autor
from .serializes import BuchSerializer

class BücherAPIView(generics.ListAPIView):
    queryset = Buch.objects.all()
    serializer_class = BuchSerializer