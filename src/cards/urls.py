from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('cards',views.CardsView,basename='cards')
router.register("card-images",views.CardImagesView,basename='card-images')
router.register('decks',views.DeckView,basename="decks")
app_name = 'cards'
urlpatterns = [ 
    
    *router.urls
    
]

