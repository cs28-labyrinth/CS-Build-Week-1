from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

r_outside = Room(title="Maze Entrance",
               description="The entry to the maze beckons you")
r_foyer = Room(title="The Great Hall", description="""Dim light filters into this Great Hall. Dusty
passages lead to your next adventure.""")
r_overlook = Room(title="The Minstrel's Gallery", description="""Musicians and jesters are what you may find here.""")
r_narrow = Room(title="The Throne Room", description="""This room is the most opulent. The smell of gold permeates the air.""")
r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Look around and check to see if there is any treasure left!""")

rooms = [
  {"title":"Maze Entrance", "description":"The entry to the maze beckons you"},
  {"title":"The Great Hall", "description":"""Dim light filters into this Great Hall. Dusty
passages lead to your next adventure."""},
{"title":"The Minstrel's Gallery", "description":"""Musicians and jesters are what you may find here."""},
{"title":"The Throne Room", "description":"""This room is the most opulent. The smell of gold permeates the air."""},
{"title":"Treasure Chamber", "description":"""You've found the long-lost treasure
chamber! Look around and check to see if there is any treasure left!"""}]


r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()

# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

