from django.contrib.auth.models import User
from adventure.models import Player, Room as Rm
import random

Rm.objects.all().delete()

x=10
y=10
width= x * 2 +1
height= y * 2 +1

class Room():
  def __init__(self,i,j):
    self.i = i
    self.j = j
    self.visitted= False
    self.prev = None
    self.move_list=[]
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None
    self.rm = Rm()
    # @property
    # def n_to(self):
    #   return self.rm.n_to
    # @property
    # def s_to(self):
    #    return self.rm.s_to
    # @property
    # def w_to(self):
    #   return self.rm.w_to
    # @property
    # def e_to(self):
    #    return self.rm.e_to
    # @n_to.setter
    # def n_to(self, value):
    #     self.rm.n_to = value
    # @s_to.setter
    # def s_to(self, value):
    #     self.rm.s_to = value
    # @w_to.setter
    # def w_to(self, value):
    #     self.rm.w_to = value
    # @e_to.setter
    # def e_to(self, value):
    #     self.rm.e_to = value

grid = [["0" for i in range(width)] for i in range(height)]

rooms = [
  {"title":"Outside Cave Entrance", "description":"North of you, the cave mount beckons"},
  {"title":"Foyer", "description":"""Dim light filters in from the south. Dusty
passages run north and east."""},
{"title":"Grand Overlook", "description":"""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""},
{"title":"Narrow Passage", "description":"""The narrow passage bends here from west
to north. The smell of gold permeates the air."""},
{"title":"Treasure Chamber", "description":"""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""}]

for i in range(1, height, 2):  
  for j in range(1, width, 2):
      rn = random.choice(rooms)
      grid[i][j] = Room(i,j)
      grid[i][j].rm.title = rn["title"]
      grid[i][j].rm.description = rn["description"]
      grid[i][j].rm.save()

def find_not_visitted_rooms(i=1,j=1):
  current = grid[i][j]
  current.visitted = True
  if i > 1 and not grid[i-2][j].visitted:
    grid[i-2][j].prev=current
    current.move_list.append(grid[i-2][j])
  if i < height - 2 and not grid[i+2][j].visitted:    
    grid[i+2][j].prev=current
    current.move_list.append(grid[i+2][j])
  if j > 1 and not grid[i][j-2].visitted:
    grid[i][j-2].prev=current
    current.move_list.append(grid[i][j-2])
  if j < width - 2 and not grid[i][j+2].visitted:
    grid[i][j+2].prev=current
    current.move_list.append(grid[i][j+2])
  return current.move_list

def connect_room(rm):
  if not rm.visitted:
     rm.visitted = True
     a = rm.i - rm.prev.i
     b = rm.j - rm.prev.j
     grid[rm.prev.i + a //2][rm.prev.j + b //2]= " "     
     # from prev to east
     if b == 2:
      #  rm.prev.e_to = grid[rm.i][rm.j]
      #  grid[rm.i][rm.j].w_to = rm
       rm.prev.rm.connectRooms(grid[rm.i][rm.j].rm, "e")
       grid[rm.i][rm.j].rm.connectRooms(rm.prev.rm, "w")
     # from prev to west
     elif b == -2:
      #  rm.prev.w_to = grid[rm.i][rm.j]
      #  grid[rm.i][rm.j].e_to = rm
       rm.prev.rm.connectRooms(grid[rm.i][rm.j].rm, "w")
       grid[rm.i][rm.j].rm.connectRooms(rm.prev.rm, "e")
     elif a == 2:
      #  rm.prev.s_to = grid[rm.i][rm.j]
      #  grid[rm.i][rm.j].n_to = rm
       rm.prev.rm.connectRooms(grid[rm.i][rm.j].rm, "s")
       grid[rm.i][rm.j].rm.connectRooms(rm.prev.rm, "n")

 
     elif a == -2:
      #  rm.prev.n_to = grid[rm.i][rm.j]
      #  grid[rm.i][rm.j].s_to = rm
       rm.prev.rm.connectRooms(grid[rm.i][rm.j].rm, "n")
       grid[rm.i][rm.j].rm.connectRooms(rm.prev.rm, "s")
     


def recur(stack):
  while len(stack):
    random.shuffle(stack)
    rm = stack.pop()
    connect_room(rm)
    recur(find_not_visitted_rooms(rm.i, rm.j))

recur(find_not_visitted_rooms())



for i in range(height):
  for j in range(width):
    if i == 1 and j == 1:
      print("●", end =" ")
    elif i == height - 2 and j == width - 2:
      print("★", end=" ")
    elif isinstance(grid[i][j], Room) or grid[i][j] == " ": 
      if isinstance(grid[i][j], Room):
        grid[i][j].rm.save()
      print(" ", end= " ")
    else:
      print(grid[i][j], end=" ")
  print()


players=Player.objects.all()
for p in players:
  p.currentRoom=grid[1][1].rm.id
  p.save()

  
