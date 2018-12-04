
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
    
    return (leftIndex, topIndex, width, height)

print interpret("#2 @ 3,1: 4x4")
    
