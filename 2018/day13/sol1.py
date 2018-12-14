class TileEntity(object):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

        self.l = EmptyTile(X, Y)
        self.r = EmptyTile(X, Y)
        self.d = EmptyTile(X, Y)
        self.u = EmptyTile(X, Y)

    def __str__(self):
        return str((self.X, self.Y))

    def left(self):
        return self.l

    def right(self):
        return self.r
    
    def down(self):
        return self.d
    
    def up(self):
        return self.u


class Cart(object):
    

    def __init__(self, currentTile, direction):
        self.currentTile = currentTile
        self.directions = ["left", "up", "right", "down"]
        self.direction = self.directions.index(direction)
        self.turnOption = "right"
        
    def __str__(self):
        return self.currentTile.__str__()

    def turn(self, option):
        if option == "left":
            self.direction = (self.direction - 1) % 4
        elif option == "right":
            self.direction = (self.direction + 1) % 4
        else:
            self.direction = self.direction 

    def option(self):
        if self.turnOption == "right":
            self.turnOption = "left"
        elif self.turnOption == "left":
            self.turnOption = "straight"
        else:
            self.turnOption = "right"
        
        return self.turnOption
    
    def dirn(self):
        return self.directions[self.direction]
        

    def move(self):
        # Move the cart
        if self.dirn() == "left":
            self.currentTile = self.currentTile.left()
        elif self.dirn() == "up":
            self.currentTile = self.currentTile.up()
        elif self.dirn() == "right":
            self.currentTile = self.currentTile.right()
        else:
            self.currentTile = self.currentTile.down()
        
        # Turn if necessary
        self.turn(self.currentTile.direction(self))    
            
            
    
class EmptyTile(TileEntity):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    
    def direction(self, cart):
        return "straight"


class StraightTile(TileEntity):    
    def __init__(self, X, Y):
        TileEntity.__init__(self, X, Y)

    def direction(self, cart):
        return "straight"
    
    
class TurnTile(TileEntity):
    # Faces is a 2-element array/tuple as follows:
    # faces[0] is "left", faces[1] is "right"

    def __init__(self, X, Y, faces):
        TileEntity.__init__(self, X, Y)
        self.faces = faces

    # Figure out which way the cart will be forced to turn
    def direction(self, cart):
        if cart.dirn() in self.faces[0]:
            return "right"
        else:
            return "left"
    
class IntersectionTile(TileEntity):
    def __init__(self, X, Y):
        TileEntity.__init__(self, X, Y)
        

    # Figure out which way the cart will be forced to turn
    def direction(self, cart):
        return cart.option()


# Start by Reading in puzzle input
with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip("\n") for line in lines]
    f.close()


# Create a grid first, to understand the puzzle input
grid = [[None for i in range(len(row))] for row in lines]
carts = []
for yIndex in range(len(lines)):
    row = lines[yIndex]
    for xIndex in range(len(row)):
        if row[xIndex] == " ":
            tile = EmptyTile(xIndex, yIndex)
        elif row[xIndex] == "+":
            tile = IntersectionTile(xIndex, yIndex)
        elif row[xIndex] == "\\":
            tile = TurnTile(xIndex, yIndex, (["right", "left"], ["down", "up"]))
        elif row[xIndex] == "/":
            tile = TurnTile(xIndex, yIndex, (["down", "up"], ["right", "left"]))
        elif row[xIndex] == ">":
            tile = StraightTile(xIndex, yIndex)
            cart = Cart(tile, "right")
            carts.append(cart)
        elif row[xIndex] == "<":
            tile = StraightTile(xIndex, yIndex)
            cart = Cart(tile, "left")
            carts.append(cart)
        elif row[xIndex] == "^":
            tile = StraightTile(xIndex, yIndex)
            cart = Cart(tile, "up")
            carts.append(cart)
        elif row[xIndex] == "v":
            tile = StraightTile(xIndex, yIndex)
            cart = Cart(tile, "down")
            carts.append(cart)
        else:
            tile = StraightTile(xIndex, yIndex)

        grid[yIndex][xIndex] = tile

# Connect components of the grid together

print "\n".join([str([str(item) for item in row]) for row in grid])

# First row
for xIndex in range(len(grid[0])):
    if xIndex != len(grid[0]) - 1:
        grid[0][xIndex].r = grid[0][xIndex + 1]
    if xIndex != 0:
        grid[0][xIndex].l = grid[0][xIndex - 1]
    
    grid[0][xIndex].d = grid[1][xIndex]

# Middle rows
for yIndex in range(1, len(grid) - 1):
    for xIndex in range(len(grid[yIndex])):
        if xIndex != len(grid[yIndex]) - 1:
            grid[yIndex][xIndex].r = grid[yIndex][xIndex + 1]
        if xIndex != 0:
            grid[yIndex][xIndex].l = grid[yIndex][xIndex - 1]


        grid[yIndex][xIndex].d = grid[yIndex + 1][xIndex]
        grid[yIndex][xIndex].u = grid[yIndex - 1][xIndex]

# Last row
for xIndex in range(len(grid[-1])):
    if xIndex != len(grid[-1]) - 1:
        grid[-1][xIndex].r = grid[-1][xIndex + 1]
    if xIndex != 0:
        grid[-1][xIndex].l = grid[-1][xIndex - 1]
    
    grid[-1][xIndex].u = grid[-2][xIndex]

# Mesh fully connected, time to move carts

# Grab all the cart locations at once
def cartLocations(carts):
    locations = []
    for cart in carts:
        loc = (cart.currentTile.X, cart.currentTile.Y)
        locations.append(loc)
    return locations


locations = cartLocations(carts)
while len(locations) == len(set(locations)):
    for cart in carts:
        cart.move()
    locations = cartLocations(carts)


print locations


