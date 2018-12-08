with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip().split(" ") for line in lines]
    lines = [tuple([line[1], line[7]]) for line in lines]
    f.close()

# This problem is a graph-based problem... with some hints of topological sort involved.

# Convert into a adjacency list
graph = {}
nodes = set([])
for tuple in lines:
    if tuple[1] not in graph:
        graph[tuple[1]] = []
    
    graph[tuple[1]].append(tuple[0])
    nodes.add(tuple[1])
    nodes.add(tuple[0])


seen = set([])
unexplored = nodes
order = []
while len(unexplored) != 0:
    # Search for a node with no additional requirements
    possible = []
    for node in unexplored:
        if node not in graph:
            possible.append(node)
    possible.sort()
    
    # pick the first one, and then modify the adjacency list
    chosen = possible[0]
    unexplored.remove(chosen)
    order.append(chosen)
    for g in graph.keys():
        if chosen in graph[g]:
            graph[g].remove(chosen)
        if graph[g] == []:
            del graph[g]
    
print order
print "".join(order)    
