from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Cards,Deck,CardImages
from django import forms


class DeckSerializer(serializers.ModelSerializer):
    total_cards = serializers.SerializerMethodField()

    class Meta:
        model = Deck
        fields = ('id','name','user','total_cards')


    def get_total_cards(self,instance):
        return instance.total_cards

class CardImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardImages
        fields = ('id','front','back','image','card')

    def validate(self, attrs):
        if attrs['back'] == attrs['front']:
            raise ValidationError('Image should be for back or for front')
        return super().validate(attrs)
    
    
class CardsSerializer(serializers.ModelSerializer):
    photos = CardImagesSerializer(source='cardimages_set',many=True,read_only=True)

    class Meta:
        model = Cards
        fields = ('id','front_text','back_text','photos','deck')
      
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response