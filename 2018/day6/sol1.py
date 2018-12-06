with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip().split(", ") for line in lines]
    lines = [tuple([int(line[0]), int(line[1])]) for line in lines]
    f.close()

'''
First attempt


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
    

'''

# Second Attempt

# Use the same grid, but this time let coordinate figure out for themselves, which one they are closest to

grid = [[None for i in range(0, 400)] for j in range(0, 400)]

def manhattanDist(t1, t2):
    return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        closestSoFar = lines[0]
        closestDist = manhattanDist((i,j), lines[0])
        dists = [closestDist]
        for line in lines:
            # ignore first, because done already
            if line != lines[0]:
                d = manhattanDist((i,j), line)
                if d < closestDist:
                    closestDist = d
                    closestSoFar = line
                dists.append(d)
       # print (i,j)
       # print dists
       # print "-----------"
        if dists.count(closestDist) > 1:
            grid[i][j] = "(-, -)"
        if grid[i][j] == None:
            grid[i][j] = closestSoFar


print "\n".join([", ".join([str(item) for item in row]) for row in grid])

# Exclude the ones on the edges, because those will go out to infinity
excluded = set()
for item in grid[0]:
    excluded.add(item)
for item in [row[0] for row in grid]:
    excluded.add(item)
for item in grid[-1]:
    excluded.add(item)
for item in [row[-1] for row in grid]:
    excluded.add(item)

#print excluded

# exclude the excluded set
lines = [line for line in lines if line not in excluded]

# count up the area
final_counts = {}
for line in lines:
    final_counts[line] = 0

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] in final_counts:
            final_counts[grid[i][j]] += 1

print final_counts

print max(final_counts.values())
