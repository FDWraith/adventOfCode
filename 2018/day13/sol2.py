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
    def __init__(self, X, Y, p):
        TileEntity.__init__(self, X, Y)
        self.p = p

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
            tile = StraightTile(xIndex, yIndex, "-")
            cart = Cart(tile, "right")
            carts.append(cart)
        elif row[xIndex] == "<":
            tile = StraightTile(xIndex, yIndex, "-")
            cart = Cart(tile, "left")
            carts.append(cart)
        elif row[xIndex] == "^":
            tile = StraightTile(xIndex, yIndex, "|")
            cart = Cart(tile, "up")
            carts.append(cart)
        elif row[xIndex] == "v":
            tile = StraightTile(xIndex, yIndex, "|")
            cart = Cart(tile, "down")
            carts.append(cart)
        else:
            tile = StraightTile(xIndex, yIndex, row[xIndex])

        grid[yIndex][xIndex] = tile

# Connect components of the grid together

# print "\n".join([str([str(item) for item in row]) for row in grid])

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

# print out the grid, with the carts
def print_grid(g, carts):
    s = [[None for i in range(len(row))] for row in grid]
    for yIndex in range(len(grid)):
        for xIndex in range(len(grid[yIndex])):
            tile = grid[yIndex][xIndex]
            
            if isinstance(tile, StraightTile):
                pixel = tile.p
            elif isinstance(tile, TurnTile):
                if tile.faces[0] == ["right", "left"]:
                    pixel = "\\"
                else:
                    pixel = "/"
            elif isinstance(tile, IntersectionTile):
                pixel = "+"
            else:
                pixel = " "

            cartHere = False            
            for cart in carts:
                if cart.currentTile == tile:
                    if cartHere:
                        pixel = "X"
                    else:
                        cartHere = True
                        if cart.dirn() == "up":
                            pixel = "^"
                        elif cart.dirn() == "down":
                            pixel = "v"
                        elif cart.dirn() == "left":
                            pixel = "<"
                        elif cart.dirn() == "right":
                            pixel = ">"
            s[yIndex][xIndex] = pixel
    return "\n".join(["".join(row) for row in s])

def sort_key(c):
    return c.currentTile.Y * 1000000 + c.currentTile.X

locations = cartLocations(carts)
'''
# print locations
tick = 0
cartIndex = 0
while len(carts) != 1:
    if cartIndex == 0:
        print print_grid(grid, carts)
        print "----------------------------"

    cart = carts[cartIndex]
    cart.move()
    locations = cartLocations(carts)

    # Two carts have collided
    if len(locations) != len(set(locations)):
        collisions = [locations.count(loc) > 1 for loc in locations]
        loc = [loc for loc in locations if locations.count(loc) > 1][0]
        diff = 0
        for index in range(len(collisions)):
            if collisions[index]:
                carts[index] = None
                if index <= cartIndex:
                    diff += 1
        while None in carts:
            carts.remove(None)
        cartIndex -= diff
        locations = cartLocations(carts)
        print "collision at " + str(loc) + " during Tick " + str(tick)

    carts.sort(key = sort_key) 
    # print len(carts)
    cartIndex = (cartIndex + 1) % (len(carts))
    # if cartIndex == 0:
    #     tick += 1

'''

tick = 0
while len(carts) != 1:

    # print print_grid(grid, carts)
    # print "-------------------------------------"

    toRemove = [] 
    for cart in carts:
        cart.move()

        locations = cartLocations(carts)
        # check for collision
        collisions = [loc for loc in locations if locations.count(loc) > 1]
        if (cart.currentTile.X, cart.currentTile.Y) in collisions:

            collided = [c for c in carts if c.currentTile == cart.currentTile]
            for c in collided:
                toRemove.append(c)
            
    
    for cart in toRemove:
        carts.remove(cart)
    
    carts.sort(key = sort_key)
    locations = cartLocations(carts)
    tick += 1

# last cart gets to move one last time
# carts[0].move()
# locations = cartLocations(carts)

print print_grid(grid,carts)

print locations

# print tick
