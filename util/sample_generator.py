import random

class Room:
    def __init__(self, id, name, description, x, y):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
    def __repr__(self):
        if self.e_to is not None:
            return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
        return f"({self.x}, {self.y})"
    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to", self)
    def get_room_in_direction(self, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        return getattr(self, f"{direction}_to")
    def check_connections(self, direction):
      if getattr(self, f"{direction}_to"):
        return True
      return False

      


############## PSEUDOCODE ---- OUT OF DATE
#### Start at corner 00
### Based upon the fact that connect_rooms needs a room object, need to do a full pass of all locations, create rooms, then do the pass to connect them.
## two directions aren't possible
## need to check if x == 0, or x == width // Blocks connections: y-1, x+1
## need to check if y == 0, or y == height // Blocks connections: x-1, y+1
## else
## roll all chances

## check if room has connection?? skip steps based on # of connections
#### Room connections betting? =>
## 100% to get first connection
## 85% to get second connection
## 60% to get third
## 10% to get 4th


### Roll for room Type
# # % of pie
# # out of 10?
# # 4?
# Treasure room = 0-1
# Encounter = 3-5
# Corridor = 7-10

## can_n: y-1, x == 0
## can_e: x+1, x == width
## can_s: y+1, y == height
## can_w: x-1, y == 0

## if x == width,
## reset position to x=0, y+=1, 
## else x += 1

## repeat until done




class World:
  def __init__(self):
    self.grid = None
    self.width = 0
    self.height = 0
  def generate_rooms(self, size_x, size_y, num_rooms):
    '''
    Fill up the grid, bottom to top, in a zig-zag pattern
    '''

    # Initialize the grid
    self.grid = [None] * size_y
    self.width = size_x
    self.height = size_y
    for i in range( len(self.grid) ):
      self.grid[i] = [None] * size_x
    print(self.grid)

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
        self.grid[y][x] = room
        x += 1
        room_count = room_count + 1

        # print(x, y)
      ## Create exit case of last room
      elif y < indexed_height and x == indexed_width:
        # print('first elif')
        # print(x, y)
        room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
        self.grid[y][x] = room
        y += 1
        x = 0
        room_count = room_count + 1
        # print(x, y)
      elif x < indexed_width:
        # print('second elif')
        # print(x, y)
        room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
        self.grid[y][x] = room
        x += 1
        room_count = room_count + 1
        # print(x, y)
      elif y == indexed_height and x == indexed_width:
        # print('LAST ONE')
        # print(x, y)
        room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
        self.grid[y][x] = room
        # print(room_count, num_rooms)
        room_count = room_count+1
      else:
        print('Ive fucked something')

    ## reset variables
    # room_count = 0
    # x = 0
    # y = 0

    print('rooms created')
    print(self.grid)
    print(self.grid[3][4].x)

### helper for directions
    ## can_n: y-1, x == 0
    ## can_e: x+1, x == width
    ## can_s: y+1, y == height
    ## can_w: x-1, y == 0
    
    #### Now that rooms are created, we can connect them randomly
    for row in self.grid:
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
              new_room = self.grid[new_y][new_x]
              print(new_direction)
              room.connect_rooms(new_room, new_direction)
            connection_attempts = connection_attempts - 1
            connection_complete = True


    # random(1-10) # 10 ^ 2 directions 2 connections

    # - What is possible
    # - What already is
    # - Random Chance % of # of connections
    # - Randomly Roll the direction of those connections

    # MAKE THOSE CONNECTIONS



###################OLD
    # direction = 1  # 1: east, -1: west


    # # While there are rooms to be created...
    # #??? Do I need this?? What is this initializing???
    # while room_count < num_rooms:

    #   # 
    #   # Need to create edge/corner cases to ensure it doesn't try to connect to things that aren't there
    #   # 
    #   if direction > 0 and x < size_x - 1:
    #     room_direction = "e"
    #     x += 1
    #   elif direction < 0 and x > 0:
    #     room_direction = "w"
    #     x -= 1
    #   else:
    #     # If we hit a wall, turn north and reverse direction
    #     room_direction = "n"
    #     y += 1
    #     direction *= -1

    #   # Create a room in the given direction
    #   room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
    #   # Note that in Django, you'll need to save the room after you create it

      # Save the room in the World grid




      #### OLD
      # # Connect the new room to the previous room
      # if previous_room is not None:
      #   previous_room.connect_rooms(room, room_direction)

      # # Update iteration variables
      # previous_room = room
      # room_count += 1



  def print_rooms(self):
    '''
    Print the rooms in room_grid in ascii characters.
    '''

    # Add top border
    str = "# " * ((3 + self.width * 5) // 2) + "\n"

    # The console prints top to bottom but our array is arranged
    # bottom to top.
    #
    # We reverse it so it draws in the right direction.
    reverse_grid = list(self.grid) # make a copy of the list
    reverse_grid.reverse()
    for row in reverse_grid:
        # PRINT NORTH CONNECTION ROW
        str += "#"
        for room in row:
            if room is not None and room.n_to is not None:
                str += "  |  "
            else:
                str += "     "
        str += "#\n"
        # PRINT ROOM ROW
        str += "#"
        for room in row:
            if room is not None and room.w_to is not None:
                str += "-"
            else:
                str += " "
            if room is not None:
                str += f"{room.id}".zfill(3)
            else:
                str += "   "
            if room is not None and room.e_to is not None:
                str += "-"
            else:
                str += " "
        str += "#\n"
        # PRINT SOUTH CONNECTION ROW
        str += "#"
        for room in row:
            if room is not None and room.s_to is not None:
                str += "  |  "
            else:
                str += "     "
        str += "#\n"

    # Add bottom border
    str += "# " * ((3 + self.width * 5) // 2) + "\n"

    # Print string
    print(str)


w = World()
width = 10
height = 10
num_rooms = width * height
w.generate_rooms(width, height, num_rooms)
w.print_rooms()
print(w.grid[4][5].check_connections('n'))
print(w.grid[4][5].check_connections('e'))
print(w.grid[4][5].check_connections('s'))
print(w.grid[4][5].check_connections('w'))

print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
