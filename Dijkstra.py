import sys, time



#Based on https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

def printPath(paths, j):
    #Recursion to print path
    # Base Case : If j is source
    if paths[j] == -1:
        print(j,",", end='',sep='')
        return
    printPath(paths, paths[j])
    print(j,",", end='',sep='')
def printSolution(dist, paths):
    print("Vertex \tDistance from Source")
    for node in range(nodes):
        print("\n%d \t\t%s \t\t\t\t\t" % ( node, dist[node]), "[ ", end='')
        if dist[node] != float("Inf"):
            printPath(paths, node)
        else:
            print('inf', end='')
        print("]", end='')

def minDistance(dist, sptSet):
    # Initilaize minimum distance for next node
    min = sys.maxsize
    min_index=0

    # Search not nearest vertex not in the
    # shortest path tree
    for v in range(nodes):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index

def dijkstra(adjacencyMatrix, Vnum):
    startTime = time.perf_counter()
    global nodes
    nodes=Vnum
    dist = [float("Inf")] * nodes
    # Distance of source = 0
    dist[0] = 0
    sptSet = [False] * nodes

    # Create list of paths
    paths = [-1] * nodes


    for node in adjacencyMatrix:
        # Pick the minimum distance vertex from
        # the set of vertices not yet processed.
        # u is always equal to src in first iteration
        u = minDistance(dist, sptSet)

        # Put the minimum distance vertex in the
        # shotest path tree
        sptSet[u] = True

        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # the vertex in not in the shotest path tree
        for v in range(nodes):
            if adjacencyMatrix[u][v] > 0 and sptSet[v] == False and \
                    dist[v] > dist[u] + adjacencyMatrix[u][v]:
                dist[v] = dist[u] + adjacencyMatrix[u][v]
                paths[v] = u



    stopTime = time.perf_counter()
    print("\nRuntime: ", ((stopTime - startTime)*1000),"\n")
    printSolution(dist, paths)