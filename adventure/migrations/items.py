from django.db import models
from django.contrib.auth.models import User
from models import Room, Player
from item_generator import Item
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid
import math
import random

class Items(models.Model):
    
    item_name = models.CharField(max_length=20, default="DEFAULT_ITEM")
    item_description = models.CharField(max_length=200, default="DEFAULT DESCRIPTION")
    

    # def __str__(self):
    #     return self.name
    def unsetItem(self):
        
        self.save()
    

class Treasures(models.Model):
        
    name = models.CharField(max_length=20, default="DEFAULT NAME")
    description = models.CharField(max_length=200, default="DEFAULT DESCRIPTION")
    value = models.IntegerField(default=1)
    
    #method so the treasures get added to rooms on init
    def roll_treasure(self):
        
        treasure_list = [
            ("gold", "This is a tiny piece of gold", 100),
            ("steel ore", "This is a piece of gold", 50),
            ("emerald", "This is an emerald gem", 250),
            ("diamond", "This is a large diamond", 500),
            ("Hide of the Nemean", "This is the hide of a powerful lion", 600),
            ("Golden Fleece", "This is the fleece of the ram, Chrysomallus", 400)
            
            
            
            
        ]  
        # Change this to a random method 
        self.name = treasure_list[min(self.level - 1, len(treasure_list) - 1)][0]
        
        #Not sure if this is needed?
        self.description = treasure_list[min(self.level - 1, len(treasure_list) - 1)][1]
        self.aliases = f"treasure,{self.name}"
        
        self.save()