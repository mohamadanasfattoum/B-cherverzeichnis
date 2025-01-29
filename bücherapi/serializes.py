from rest_framework import serializers
from .models import Buch, Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['name']


class BuchSerializer(serializers.ModelSerializer):
    autors = AutorSerializer(many = True)
    class Meta:
        model = Buch
        fields = '__all__'
