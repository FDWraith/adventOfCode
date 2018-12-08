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

# Some values
k = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
times = {k[index] : index + 61 for index in range(0,len(k))}

workers = [None, None, None, None, None]
working = []

timer = 0
seen = set([])
unexplored = nodes
order = []
while len(unexplored) != 0 or len(working) != 0:    
    # Check on the workers
    for workerIndex in range(0,len(workers)):
        
        worker = workers[workerIndex]

        # If a worker is done working
        if worker != None and worker[1] == 0:
            jobDone = worker[0]
            working.remove(jobDone)
            unexplored.remove(jobDone)
            order.append(jobDone)
            workers[workerIndex] = None
            for g in graph.keys():
                if jobDone in graph[g]:
                    graph[g].remove(jobDone)
                if graph[g] == []:
                    del graph[g]
    
    # Search for a node with no additional requirements
    possible = []
    for node in unexplored:
        if node not in graph and node not in working:
            possible.append(node)
    possible.sort()
                    
    # Assign new work to workers
    for workerIndex in range(0,len(workers)):
        worker = workers[workerIndex]
         
        # If there is still work to be done
        if len(possible) != 0:
            if worker == None:
                workers[workerIndex] = [possible[0], times[possible[0]]]
                working.append(possible[0])
                possible.remove(possible[0])
    
    print workers
    print working

    # Get some work done
    for worker in workers:
        if worker != None:
            worker[1] -= 1
    timer += 1
    
print order
print "".join(order)    
print timer - 1
