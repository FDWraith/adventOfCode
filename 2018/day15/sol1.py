# Sort Key for most things (yIndex takes priority)
def reading_order(tile):
    return tile.Y * 1000000 + tile.X

class Tile(object):
    '''
    The Tile class is a placeholder class with default methods for tile instances
    '''

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.passable_ = False

    def position(self):
        return (self.X, self,Y)

    def passable(self):
        '''Can a Unit stand on this tile?'''
        return self.passable_

class OpenTile(Tile):
    '''
    An Open Tile represents a place where units can pass through / stand on
    '''
    
    def __init__(self, X, Y):
        Tile.__init__(X, Y)
        self.has_unit = False

    def __str__(self):
        return "."

    def passable(self):
        if has_unit:
            return False
        else:
            return True

    def add_unit(self):
        self.has_unit = True
    
    def remove_unit(self):
        self.has_unit = False
    

class WallTile(Tile):
    '''
    A Wall tile is impassable for units
    '''
    
    def __init__(self, X, Y):
        Tile.__init__(X, Y)    

    
    def __str__(self):
        return "#"

    # Passable inherited

class Unit(object):
    '''
    A Unit has HitPoints (HP), Attack Power (Attk), and the tile it is standing on 
    (currentTile)
    '''

    def __init__(self, tile, HP, atk):
        self.currentTile = tile
        self.HP = HP
        self.attk = atk
        self.dead = True if HP <= 0 else False
        
        if not self.is_dead():
            tile.add_unit()

    def position(self):
        return self.currentTile.position()
            
    def attack(self, other):
        assert isinstance(other, Unit)
        other.get_hit(self.attk)
        
    def get_hit(self, hitpoints):
        assert isinstance(hitpoints, int)
        self.HP -= attk
        self.dead = True if HP <= 0 else False        

    def is_dead(self):
        return self.dead

    def move_to(self, new_tile):
        if not self.is_dead() and new_tile.passable():
            self.currentTile.remove_unit()
            self.currentTile = new_tile
            self.currentTile.add_unit()
    

class Board(object):
    '''
    Board Class is responsible for organizing most of the simulation
    
    It has access to the grid, and is aware of individual units and etc. 
    '''
    

    def __init__(self, grid_string):
        self.grid = [[c for c in row.strip()] for row in grid_string]
        
        # Convert the grid from character representations to tile representations
        self.elves = []
        self.goblins = []
        for row, yIndex in enumerate(grid):
            for item, xIndex in enumerate(row):
                if item == ".":
                    tile = OpenTile(xIndex, yIndex)
                elif item == "E":
                    tile = OpenTile(xIndex, yIndex)
                    elf = Unit(tile, 3, 200)
                    self.elves.append(elf)
                elif item == "G":
                    tile = OpenTile(xIndex, yIndex)
                    goblin = Unit(tile, 3, 200)
                    self.goblins.append(goblin)
                else:
                    tile = WallTile(xIndex, yIndex)
                
                self.grid[yIndex][xIndex] = tile
        
        self.currentRound = 0
        self.elves = self.sort_units(self.elves)
        self.goblins = self.sort_units(self.goblins)
        
        
    def sort_units(units):        
        def tiled_order(unit):
            return reading_ordert(unit.currentTile)
        
        units.sort(key = tiled_order)
        return units

    def execute_round():
        elves = self.elves
        goblins = self.goblins
        grid = self.grid
        
        

        
