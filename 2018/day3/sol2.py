# Copied from Part 1

# Part 2 solution idea: reiterate thru array, to check again after everything

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
    _id = data[0].strip("#")
    
    return (int(leftIndex), int(topIndex), int(width), int(height), _id)

# update array to record changed places
for line in lines:
    newLine = interpret(line)
    for i in range(newLine[0], newLine[0] + newLine[2]):
        for j in range(newLine[1], newLine[1] + newLine[3]):
            array[i][j] += 1
   
# reiterate to check for non-overlapping
for line in lines:
    newLine = interpret(line)
    nonOverlap = True
    for i in range(newLine[0], newLine[0] + newLine[2]):
        for j in range(newLine[1], newLine[1] + newLine[3]):
            if array[i][j] != 1:
                nonOverlap = False
    if nonOverlap:
        print newLine[4] # print out the id of non overlapping piece


