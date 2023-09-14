from typing import Iterable, Optional
from django.db import models
from users.models import CustomUser
from django.core.exceptions import ValidationError

# Create your models here.

def user_based_uploader(instance,filename):
        if instance.back:
            return f'{instance.card.user.username}/back_images/{filename}'
        return f'{instance.card.user.username}/front_images/{filename}'
    

class Deck(models.Model):
    '''

    Колода для флэш кард
    
    '''
    name = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    

    class Meta:
         unique_together = ("name", "user")

class Cards(models.Model):
    '''

    Флэш карты

    '''
    front_text = models.TextField()
    back_text = models.TextField()
    deck = models.ForeignKey(Deck,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class CardImages(models.Model):
    '''
    
    Images для флэш карт
    
    '''

    card = models.ForeignKey(Cards,on_delete=models.CASCADE)
    image = models.FileField(upload_to=user_based_uploader,unique=True)
    back = models.BooleanField(null=True)
    front = models.BooleanField(null=True)

    
