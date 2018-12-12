serial = 3999

def power(xCor, yCor):
    rackID = xCor + 10
    p = rackID * yCor + serial
    p = p * rackID
    p = p / 100 % 10 - 5
    return p

grid = [[power(i,j) for i in range(300)] for j in range(300)]

# Find maximum power of 3 x 3
mp = 0
for y in range(297):
    for x in range(297):
        v = sum([grid[i][j] for i in range(x,x+3) for j in range(y, y+3)])
        if v > mp:
            mp = v
            currX = x
            currY = y

print currX, currY
