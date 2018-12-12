# I really should abstract this to a utility

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    f.close()


class MovingPoint(object):
    def __init__(self):
        self.xCor = 0
        self.yCor = 0
        self.xVel = 0
        self.yVel = 0

    def __init__(self, xCor, yCor, xVel, yVel):
        self.xCor = xCor
        self.yCor = yCor
        self.xVel = xVel
        self.yVel = yVel
       
    def __str__(self):
        return str(tuple([self.xCor, self.yCor]))

    def move(self):
        self.xCor += self.xVel
        self.yCor += self.yVel
        
        return (self.xCor, self.yCor)
    
    def reverse(self):
        self.xCor -= self.xVel
        self.yCor -= self.yVel
        
        return (self.xCor, self.yCor)
    

# Initialize a list of points
points = []
for line in lines:
    line = line.split("velocity")
    position = line[0][line[0].index("<") + 1: line[0].index(">")].split(", ")
    velocity = line[1][line[1].index("<") + 1: line[1].index(">")].split(", ")
    point = MovingPoint(int(position[0]), int(position[1]), int(velocity[0]), int(velocity[1]))
    points.append(point)
    
# Temporary print statement (because regular print doesn't do this)
def print_points(pts):
    print "[ " + ", ".join([str(pt) for pt in pts]) + " ]"
    

# Idea: Bounding Box on the points (they should all be moving towards their final posiition)

# Find bounds on a list of points
def bounds(pts):
    ex = points[0] # Pick the first one to start with
    leftBound = rightBound = ex.xCor
    topBound = bottomBound = ex.yCor 
    for point in pts:
        if point.xCor < leftBound:
            leftBound = point.xCor
        if point.xCor > rightBound:
            rightBound = point.xCor
        if point.yCor > topBound:
            topBound = point.yCor
        if point.yCor < bottomBound:
            bottomBound = point.yCor
        
    return (leftBound, rightBound, topBound, bottomBound)


# Compare two bounds to see if b1 will fit in b2
def fit(b1, b2):
    return b1[0] >= b2[0] and b1[1] <= b2[1] and b1[2] <= b2[2] and b1[3] >= b2[3]

# Establish starting bounds
cap = bounds(points)

# Move points once
for point in points:
    point.move()

# New Bounds:
new = bounds(points)

counter = 0

while fit(new, cap):    
    
    cap = new

    # Move points once
    for point in points:
        point.move()
        
    new = bounds(points)
    counter += 1

print counter
