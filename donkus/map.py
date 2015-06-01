     



class Room(object):
    """represents a room in the game"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


   

# API
def generate():
    start = Room("Start", "You can go west and down a hole.")
    trees = Room("Trees", "There are trees here, you can go east.")
    dungeon = Room("Dungeon", "It's dark down here, you can go up.")
    bog = Room("Bog", "It smells of rotting vegetation.  All about you there are eyes watching.  You can go ____")
    cave = Room("Cave", "The pitch black is blinding, and there is movement nearby.   You can go ____")

    start.add_paths({'west': trees, 'down': dungeon})
    trees.add_paths({'east': start, 'south': bog })
    dungeon.add_paths({'up': start, 'down': cave})
    bog.add_paths({'east': cave })

    rooms = [start, trees, dungeon, bog, cave]

    return rooms
