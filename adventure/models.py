from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid
import sys



###########
# Room Classes
###########
### Planning phase
## Room class accepts 

## create 50 x 50 node square
## move out => in?
## or in => out


## how to save the world?
# dict with object in it?
# 0,1: <Room object />
# 


## Treasure rooms run function from items class
## How to deal with tool spawns?


## Item Class
# Tools
# Weapons

# A Value of Treasures
# B Least steps taken/per map type





##### to brute force this solution I need to create methods that find room by p.id and then also grab the current coordinates of the player to locate the room.
## Return the data of the room to the user.
## User will then select an action to take in that room
## 

""" Rooooooms """
class Room(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(max_length=500, default="DEFAULT DESCRIPTION")
    n_to = models.IntegerField(default=0)
    s_to = models.IntegerField(default=0)
    e_to = models.IntegerField(default=0)
    w_to = models.IntegerField(default=0)
    def connectRooms(self, destinationRoom, direction):
        destinationRoomID = destinationRoom.id
        try:
            destinationRoom = Room.objects.get(id=destinationRoomID)
        except Room.DoesNotExist:
            print("That room does not exist")
        else:
            if direction == "n":
                self.n_to = destinationRoomID
            elif direction == "s":
                self.s_to = destinationRoomID
            elif direction == "e":
                self.e_to = destinationRoomID
            elif direction == "w":
                self.w_to = destinationRoomID
            else:
                print("Invalid direction")
                return
            self.save()
    room_array = [
      (),
      ()
    ]
    # def playerNames(self, currentPlayerID):
    #     return [p.user.username for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]
    def playerUUIDs(self, currentPlayerID):
        return [p.uuid for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]
    def exits(self):
      exits = []
      if self.n_to is not None:
        exits.append("n")
      if self.s_to is not None:
        exits.append("s")
      if self.e_to is not None:
        exits.append("e")
      if self.w_to is not None:
        exits.append("w")
      return exits


###
# Room Types
###

class Teasure_Room(Room):
  pass

class Corridor_Room(Room):
  pass

class Encounter_Room(Room):
  pass

class Room_Room(Room):
  pass


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ### Default only works for the 10x10 field
    currentRoom = models.IntegerField(default=54)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    def initialize(self):
      if self.currentRoom == 0:
        self.currentRoom = Room.objects.first().id
        self.save()
    def room(self):
      try:
        return Room.objects.get(id=self.currentRoom)
      except Room.DoesNotExist:
        self.initialize()
        return self.room()
    def findWorld(self):
      return [r for r in Room.objects.filter(player=self.id) if r.id == player]
      # for rooms in Room.objects.filter(player=self):
      #   if player.id in rooms.player_id

@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()





