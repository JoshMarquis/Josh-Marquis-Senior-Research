
import Graph, Dijkstra,BellmanFord

if __name__ == "__main__":


    ###FOR ADJACENCY MATRIX
    #value = weight, index=node dest
    #i.e. [0,0,0,5] this node is connected to node 4 with a cost of 5

    ###FOR WEIGHTED EDGES LIST
    #each edge is a row with three values, [source, dest, weight]

    print("Enter desired number of nodes")
    nodes=int(input())
    print("Enter desired completeness percentage as a decimal, i.e. 15% = .15")
    cGoal = float(input())
    print("Note: If program runs for several seconds, try changing the distance threshold in Graph.py to reach the desired completeness more easily")
    adjacencyMatrix, weightedEdges = Graph.generateGraph(nodes,cGoal)


    #Find shortest path using Dijkstra's algorithm
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Dijkstra's Algorithm")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")

    Dijkstra.dijkstra(adjacencyMatrix,nodes)


    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Bellman-Ford Algorithm")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")

    BellmanFord.BellmanFord(weightedEdges,nodes)
