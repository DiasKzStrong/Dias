from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Prefetch,F,Count
from users.models import CustomUser
from .mixins import *
from .models import Cards 
from .serializers import *
# Create your views here.

class CardsView(QuerySetMixin,viewsets.ModelViewSet):
    queryset = Cards.objects.all().select_related('user').select_related('deck').prefetch_related('cardimages_set') \
                                                                        .only('id','front_text','back_text','deck__id','user__id','user__username','user__email', 'deck__name')
    serializer_class = CardsSerializer
    
    permission_classes = (IsAuthenticated,)
    

class DeckView(QuerySetMixin,viewsets.ModelViewSet):
    queryset = Deck.objects.all().select_related('user').only('id','name','user__username').annotate(
        total_cards = Count(F('cards'))

    )
    serializer_class = DeckSerializer

class CardImagesView(QuerySetMixin,viewsets.ModelViewSet):
    queryset = CardImages.objects.all().select_related('card').only('id','image','back','front','card__id').prefetch_related(

        Prefetch('card',queryset=Cards.objects.all().select_related('deck').only('id'))

    )
    serializer_class = CardImagesSerializer