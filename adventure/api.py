from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json
import random
import math

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

def World_Generator(player):
  width = 10
  height = 10
  grid = None

  ######################### TODO: future solution
  ### ON init it looks for a file that's saved that's called the_labyrinth.txt
  ## If no file exists, it creates a new game and then saves that file.
  ## if new file, need to run through all world generation
  ## elif Generate world based upon save file data
  ## Hold this data somehow.

  # Initialize the grid
  size_x = width
  size_y = height
  num_rooms = width * height
  grid = [None] * size_y
  for i in range( len(grid) ):
    grid[i] = [None] * size_x
  # print(grid)

  # Start from lower-left corner (0,0)
  x = 0
  y = 0
  room_count = 0
  indexed_height = height-1
  indexed_width = width-1

  # # Start generating rooms by line until max height/width reached

  ###### Creating All Rooms
  while room_count < num_rooms:
    ## start left to right, incrementing x by 1, until x = width
    ## reset x, y+1
    ## need to create first room:
    if x == 0 and y == 0:
      # print('first if')
      # print(x, y)
      room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
      grid[y][x] = room
      x += 1
      room_count = room_count + 1

      # print(x, y)
    ## Create exit case of last room
    elif y < indexed_height and x == indexed_width:
      # print('first elif')
      # print(x, y)
      room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
      grid[y][x] = room
      y += 1
      x = 0
      room_count = room_count + 1
      # print(x, y)
    elif x < indexed_width:
      # print('second elif')
      # print(x, y)
      room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
      grid[y][x] = room
      x += 1
      room_count = room_count + 1
      # print(x, y)
    elif y == indexed_height and x == indexed_width:
      # print('LAST ONE')
      # print(x, y)
      room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
      grid[y][x] = room
      # print(room_count, num_rooms)
      room_count = room_count+1
    else:
      print('Ive fucked something')

  ## reset variables
  # room_count = 0
  # x = 0
  # y = 0

  # print('rooms created')
  # print(grid)
  # print(grid[3][4].x)

### helper for directions
  ## can_n: y-1, x == 0
  ## can_e: x+1, x == width
  ## can_s: y+1, y == height
  ## can_w: x-1, y == 0
  
  #### Now that rooms are created, we can connect them randomly
  for row in grid:
    for room in row:
      print('starting room connections')
      print(room.x, room.y)
      # Initalizing variables for examining room connections and blockers
      can_n = 'open'
      can_e = 'open'
      can_s = 'open'
      can_w = 'open'
      curr_connected = 0
      curr_x = room.x
      curr_y = room.y
      indexed_height = height-1
      indexed_width = width-1

      ## Checking current room connections
      if room.check_connections('n'):
        can_n = 'connected'
        curr_connected += 1
      if room.check_connections('e'):
        can_e = 'connected'
        curr_connected += 1
      if room.check_connections('s'):
        can_s = 'connected'
        curr_connected += 1
      if room.check_connections('w'):
        can_w = 'connected'
        curr_connected += 1

      ## Generating chance for how many connections ---- I DON'T KNOW HOW RANDOM WORKS
        ## 100% to get first connection
        ## 80% to get second connection
        ## 60% to get third
        ## 10% to get 4th

      connection_roll = random.randint(0,10)
      # print('connection_roll')
      # print(connection_roll)
      ###### TO-DO: THIS SHIT DOESN'T WORK. I DON'T UNDERSTAND PERCENT CHANCES WTF???????
      connection_attempts = 0
      if connection_roll <= 1:
        connection_attempts = 4
      elif connection_roll > 1 and connection_roll < 5:
        connection_attempts = 3
      elif connection_roll >= 5 and connection_roll < 9:
        connection_attempts = 2
      else:
        connection_attempts = 1

      ### If the amount of connections rolled == the current amount of connections, nothing left to do!
      if connection_attempts == curr_connected:
        print('were in the connect = curr check')
        pass

      ### Now to check which directions are block
      blocked = 0
      print('checking blocks')
      if curr_x == 0:
        can_s = 'blocked'
        blocked += 1
      if curr_x == indexed_width:
        can_e = 'blocked'
        blocked += 1
      if curr_y == 0:
        can_w = 'blocked'
        blocked += 1
      if curr_y == indexed_height:
        can_n = 'blocked'
        blocked += 1

      #### TO-DO: SPECIAL CASE
      ### If connection_attempts is 4 and blocked are 2, need to only check 2. if connection attempts are 2 and blocked are 2, still need to check 2
      ## how the fuck do u math that


      ### NOW IT'S TIME TO MAKE SOME CONNECTIONS, LADIES AND GENTS
      print('starting connection while loop')
      print(connection_attempts)
      while connection_attempts > 0:
        connection_complete = False
        # print('we in first while')
        while connection_complete is False:
          # print('start of second while')
          #Roll for direction  
          direction_roll = random.randint(0,3)
          # print(direction_roll)
          # set directions to array
          directions = [can_n, can_e, can_s, can_w]
          direction_array = ['n', 'e', 's', 'w']
          # print(directions[direction_roll])
          print('this is the directions roll')
          print(directions[direction_roll])
          if directions[direction_roll] == 'open':
            # print('success')
            # directions[direction_roll] = 'connected'
            ####### UAOLDFKS;LADSF HOW DOES SOME FUCKING IDIOT CONNECT ROOMS
            new_x = curr_x
            new_y = curr_y
            ## Creating new direction
            if direction_roll == 0: # N
              new_y = curr_y + 1
            if direction_roll == 1: # E
              new_x = curr_x + 1
            if direction_roll == 2: # S
              new_y = curr_y - 1
            if direction_roll == 3: # W
              new_x = curr_x - 1
            print('AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
            print(curr_x, curr_y)
            print(new_x, new_y)
            new_direction = direction_array[direction_roll]
            new_room = grid[new_y][new_x]
            print(new_direction)
            room.connect_rooms(new_room, new_direction)
          connection_attempts = connection_attempts - 1
          connection_complete = True


####
# Need an API call for creating a world
## Need to determine how to store the world data?

##

# @csrf_exempt
@api_view(["GET"])
def initialize(request):
  user = request.user
  player = user.player
  player_id = player.id
  uuid = player.uuid
  # room = player.room()
  # players = room.playerNames(player_id)
  ##TODO: Need to change this so it looks for all rooms that are associated with player.uuid
  ## Return the room at coords of player vs 
  return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players}, safe=True)


# @csrf_exempt
@api_view(["POST"])
def move(request):
    dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    nextRoomID = None
    if direction == "n":
        nextRoomID = room.n_to
    elif direction == "s":
        nextRoomID = room.s_to
    elif direction == "e":
        nextRoomID = room.e_to
    elif direction == "w":
        nextRoomID = room.w_to
    if nextRoomID is not None and nextRoomID > 0:
        nextRoom = Room.objects.get(id=nextRoomID)
        player.currentRoom=nextRoomID
        player.save()
        players = nextRoom.playerNames(player_id)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        # for p_uuid in currentPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
        # for p_uuid in nextPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'players':players, 'error_msg':""}, safe=True)
    else:
        players = room.playerNames(player_id)
        return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'error_msg':"You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error':"Not yet implemented"}, safe=True, status=500)

@api_view(["POST"])
def take(request):
  player = request.user.player
  data = json.loads(request.body)

  # cooldown_error = check_cooldown_error(player)
  # if cooldown_error is not None:
  #   return cooldown_error

  alias = data['name']
  room = player.room()
  item = room.findItemByAlias(alias, player.group)
  if player.in_dark():
    item = room.findItemAllByAlias(alias, player.group)
  cooldown_seconds = get_cooldown(player, 0.5)
  errors = []
  messages = []
  if item is None:
    cooldown_seconds += PENALTY_NOT_FOUND
    errors.append(f"Item not found: +{PENALTY_NOT_FOUND}s CD")
  elif player.strength * 2 <= player.encumbrance + item.weight:
    cooldown_seconds += PENALTY_TOO_HEAVY
    errors.append(f"Item too heavy: +{PENALTY_TOO_HEAVY}s CD")
  elif item.itemtype == "SNITCH":
    messages.append(f"A great warmth floods your body as your hand closes around the snitch before it vanishes.")
    player.snitches += 1
    item.resetSnitch()
  else:
    messages.append(f"You have picked up {item.name}")
    player.addItem(item)
  player.cooldown = timezone.now() + timedelta(0,cooldown_seconds)
  player.save()
  return api_response(player, cooldown_seconds, errors=errors, messages=messages)
