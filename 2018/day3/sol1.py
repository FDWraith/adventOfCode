
''' 
Attempt #1 

class Claim:
    def __init__(self, left, top, w, h):
        self.leftIndex = left
        self.topIndex = top
        self.width = w
        self.height = h

def overlap(a, b):
    width = 0
    height = 0
    if a.leftIndex < b.leftIndex:
        if a.leftIndex + a.width > b.leftIndex:
            width = a.leftIndex + a.width - b.leftIndex
    else:
        if b.leftIndex + b.width > a.leftIndex:
            width = b.leftIndex + b.width - a.leftIndex
    if a.topIndex < b.topIndex:
        if a.topIndex + a.height > b.topIndex:
            height = a.topIndex + a.height - b.topIndex
    else:
        if b.topIndex + b.height > a.topIndex:
            height = b.topIndex + b.height - a.topIndex

    return width * height


c1 = Claim(1,3,4,4)
c2 = Claim(3,1,4,4)
print overlap(c1,c2)

Attempt 2:

What if we stored every position with an array-like structure? 

The largest section doesn't seem to exceed 1000
'''

array = [[0 for num in range(0,1200)] for num2 in range(0,1200)]

with open("input.txt","r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    f.close()

def interpret(line):
    data = line.split(" ")
    indexes = data[-2][:-1].split(",")
    leftIndex = indexes[0]
    topIndex = indexes[1]
    size = data[-1].split("x")
    width = size[0]
    height = size[1]
    
    return (int(leftIndex), int(topIndex), int(width), int(height))

# update array to record changed places
for line in lines:
    newLine = interpret(line)
    for i in range(newLine[0], newLine[0] + newLine[2]):
        for j in range(newLine[1], newLine[1] + newLine[3]):
            array[i][j] += 1
   

# count up the number of tiles with 2 or more.
count = 0
for i in range(0, len(array)):
    for j in range(0, len(array)):
        if array[i][j] >= 2:
            count += 1

# return final result
print count

    
