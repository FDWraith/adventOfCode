serial = 3999

def power(xCor, yCor):
    rackID = xCor + 10
    p = rackID * yCor + serial
    p = p * rackID
    p = p / 100 % 10 - 5
    return p

grid = [[power(i,j) for i in range(300)] for j in range(300)]

# Attempt 1
'''
mp = 0
for s in range(1,301):
    for y in range(300 - s):
        for x in range(300 - s):
            v = sum([grid[i][j] for i in range(x,x+s) for j in range(y, y+s)])
            if v > mp:
                mp = v
                currX = x
                currY = y
                currS = s
                
print currY, currX, currS 
'''

# Attempt 2
# Need some way to record information already known...
# Layers of grids?

mp = 0
d = {} 
d[1] = grid
# print "\n".join([str(row) for row in grid])
for s in range(2,301):
    new_grid = [[0 for i in range(300)] for j in range(300)]
    for y in range(300 - s):
        for x in range(300 - s):
            # print d[s-1][x][y], [grid[x+s-1][y+i] for i in range(s)], [grid[x+i][y+s-1] for i in range(s-1)] 
            new_grid[x][y] = d[s-1][x][y] + sum([grid[x+s-1][y+i] for i in range(s)]) + sum([grid[x+i][y+s-1] for i in range(s-1)]) 
            if new_grid[x][y] > mp:
                mp = new_grid[x][y]
                currX = x
                currY = y
                currS = s
    d[s] = new_grid
    # print "\n"
    # print "\n".join([str(row) for row in new_grid])
    #if s == 3:
    #    break

print currY, currX, currS 
