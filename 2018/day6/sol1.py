with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip().split(", ") for line in lines]
    lines = [[int(line[0]), int(line[1])] for line in lines]
    f.close()

# Using a dictionary structure
# key : tuple representing coord
# value : list of next places to plot
next_plot = {}
for line in lines:
    next_plot[tuple(line)] = [tuple(line)]

print next_plot

grid = [[None for i in range(0, 400)] for j in range(0,400)]

def hasNone(g):
    o = False
    for row in g:
        o = o or None in row
    return o

# As long as the grids still has spaces
while hasNone(grid):
    for k in next_plot.keys():
        v = next_plot[k]
        k_next = []
        for val in v:
            if grid[val[0]][val[1]] == None:
                grid[val[0]][val[1]] = val
            elif grid[val[0]][val[1]] != val:
                grid[val[0]][val[1]] = "."
            
            # add neighbors to next plot
            if val[0] - 1 >= 0 and val[1] - 1 >= 0 and grid[val[0] - 1][val[1] - 1] == None:
                k_next.append([val[0] - 1, val[1] - 1])
            if val[0] - 1 >= 0 and val[1] + 1 < 400 and grid[val[0] - 1][val[1] + 1] == None:
                k_next.append([val[0] - 1, val[1] + 1])
            if val[0] + 1 < 400 and val[1] - 1 >= 0 and grid[val[0] + 1][val[1] - 1] == None:
                k_next.append([val[0] + 1, val[1] - 1])
            if val[0] + 1 < 400 and val[1] + 1 < 400 and grid[val[0] + 1][val[1] + 1] == None:
                k_next.append([val[0] + 1, val[1] + 1])

        next_plot[k] = k_next
    

