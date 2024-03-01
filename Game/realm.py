_world = {}
starting_position = (0, 0)

def room_exists(x, y):
    """Returns the room at the given x, y coordinates. None when there is no room.
    :x: = the x-coordinate in the world
    :y: = the y-coordinate in the world
    :return: = the room at the given coordinates or none if there is no room
    
    """
    
    return _world.get((x, y))

def load_rooms():
    """parses a file that describes the world space in the _world object"""
    with open('Game/resources/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            room_name = cols[x].replace('\n', '')
            if room_name == 'StartingRoom':
               global starting_position
               starting_position = (x, y)
            _world[(x, y)] = None if room_name == '' else getattr(__import__('rooms'), room_name)(x, y) 
    
    