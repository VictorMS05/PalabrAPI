from rest_framework import serializers
from .models import CatalogoPalabras

class CatalogoPalabrasSerializador(serializers.ModelSerializer):
    """"Serializador para el modelo CatalogoPalabras"""
    class Meta:
        """Clase meta para el serializador"""""
        model = CatalogoPalabras
        fields = 'id', 'palabra', 'raiz', 'letra_inicial', 'caracteres'

    def create(self, validated_data):
        # Implement the create logic here
        pass

    def update(self, instance, validated_data):
        # Implement the update logic here
        pass
