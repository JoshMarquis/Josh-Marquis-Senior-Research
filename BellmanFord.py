import time


#Based on https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/


def printPath(paths, j):
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

def BellmanFord(weightedEdges,Vnum):
    startTime = time.perf_counter()
    global nodes
    nodes = Vnum

    # Create list of paths
    paths = [-1] * nodes

    # Step 1: Initialize distances from src to all other vertices
    # as INFINITE
    dist = [float("Inf")] * nodes
    #Distance of source = 0
    dist[0] = 0

    # Step 2: Relax all edges |V| - 1 times. A simple shortest
    # path from src to any other vertex can have at-most |V| - 1
    # edges
    for _ in range(nodes -1):
        # Update dist value and parent index of the adjacent vertices of
        # the picked vertex. Consider only those vertices which are still in
        # queue
        for u,v,w in weightedEdges:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                paths[v] = u

    # Step 3: check for negative-weight cycles. The above step
    # guarantees shortest distances if graph doesn't contain
    # negative weight cycle. If we get a shorter path, then there
    # is a cycle.

    for u, v, w in weightedEdges:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return

    stopTime = time.perf_counter()
    print("\nRuntime: ", (stopTime - startTime),"\n")
    printSolution(dist,paths)