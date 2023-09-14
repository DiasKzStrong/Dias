from rest_framework import serializers
from .models import CustomUser
from cards.serializers import DeckSerializer
class UserCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username','email',)


class UserSerializer(serializers.ModelSerializer):
    decks = DeckSerializer()

    class Meta:
        model = CustomUser
        fields = ('id','username','email','decks')