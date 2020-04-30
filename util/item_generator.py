from django.db import models
from django.contrib.auth.models import User
from models import Room, Player
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid
import math
import random


       

class Rooms:
    def __init__(self, title, description, room_items=None):

        self.title = title
        self.description = description
        if room_items is None:
            self.room_items = []
        else:
            self.room_items = room_items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None



class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

        

    

class Treasure(Item): 
    def __init__(self, treasure_name, treasure_description, value, item_name, item_description):
        super().__init__(item_name, item_description)
        self.treasure_name = treasure_name
        self.treasure_description = treasure_description
        self.value = value
  
  #How to add treasure_name to room_items array?
        if room:
            #Do something to pick a random treasure from the treasure
            #treasure_randomizer
            #self.room_items.append(treasure_randomizer)

    def __str__(self):
            return f"Treasure: {self.treasure_name}, Description: {self.treasure_description}, Value: {self.value}"
    

class Players(Treasure):
    def __init__(self, user, currentRoom, uuid, username, treasure_name, treasure_description, value):
        super().__init__(treasure_name, treasure_description, value)
        self.user = user
        self.currentRoom = currentRoom
        self.uuid = uuid
        self.player_items = []

    def take_treasure(self):
        # If there is treasure in the room_items array
        if len(self.currentRoom.room_items) >= 1:
            for item in self.currentRoom.room_items:
                #take the treasure by adding it to the player_items array
                 self.player_items.append(item.treasure_name)

#List of treasures 
treasure_list = [
            Treasure("gold", "This is a tiny piece of gold", 100),
            Treasure("steel ore", "This is a piece of gold", 50),
            Treasure("emerald", "This is an emerald gem", 250),
            Treasure("diamond", "This is a large diamond", 500),
            Treasure("Hide of the Nemean", "This is the hide of a powerful lion", 600),
            Treasure("Golden Fleece", "This is the fleece of the ram, Chrysomallus", 400)
            
            
            
            
        ] 
 
 #creating a randomizer for the treasure items
 treasure_randomizer = random.choice(treasure_list)