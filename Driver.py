import time
import Graph, Dijkstra,BellmanFord

if __name__ == "__main__":
    #LATER ADD IN A PARAMETER FOR # OF NODES

    #returns a matrix of weighted edges and a list of weighted edges

    ###FOR ADJACENCY MATRIX
    #value = weight, index=node dest
    #i.e. [0,0,0,5] this node is connected to node 4 with a cost of 5

    ###FOR WEIGHTED EDGES LIST
    #each edge is a row with three values, [source, dest, weight]

    print("Enter desired number of nodes")
    nodes=int(input())
    adjacencyMatrix, weightedEdges = Graph.generateGraph(nodes)


    #Find shortest path using Dijkstra's algorithm
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Dijkstra's Algorithm")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    #startTime = time.perf_counter()
    Dijkstra.dijkstra(adjacencyMatrix,nodes)
    #stopTime = time.perf_counter()
    #print("\nRuntime: ",(stopTime - startTime))

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Bellman-Ford Algorithm")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    #startTime = time.perf_counter()
    BellmanFord.BellmanFord(weightedEdges,nodes)
    #stopTime = time.perf_counter()
    #print("\nRuntime: ",(stopTime - startTime))