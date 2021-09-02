from rest_framework import serializers
from deafApi import models

class AlphabetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alphabet
        fields = '__all__'

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Word
        fields = '__all__'