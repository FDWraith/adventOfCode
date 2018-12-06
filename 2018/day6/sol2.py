with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip().split(", ") for line in lines]
    lines = [tuple([int(line[0]), int(line[1])]) for line in lines]
    f.close()

# Use the same grid, but this time let coordinate figure out for themselves, which one they are closest to

grid = [[None for i in range(0, 400)] for j in range(0, 400)]

ans = []

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
        if sum(dists) < 10000:
            ans.append((i,j))

print len(ans)
