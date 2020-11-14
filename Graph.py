import random

import plotly.graph_objects as go
import networkx as nx
global numNodes


def generateGraph(Vnum):
    numNodes=Vnum
    #was 10, .4
    #Was .24
    G = nx.random_geometric_graph(numNodes, .30)



    # Create edges
    edge_x = []
    edge_y = []
    xtext=[]
    ytext=[]
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        xtext.append((x0+x1)/2)
        ytext.append((y0+y1)/2)
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    #Create Nodes
    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        textposition="top center",
        marker=dict(
            showscale=True,
            # colorscale options
            # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            colorscale='YlGnBu',
            reversescale=True,
            color=["rgb(255,0,0)"],
            size=20,
            #colorbar=dict(
            #    thickness=15,
            #    title='Node Connections',
            #    xanchor='left',
            #    titleside='right'
            #),
            line_width=2))
    #node Text
    node_adjacencies = []
    node_text = []
    for node, adjacencies in enumerate(G.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))
        node_text.append('Node: ' + str(node) + ', # of connections: ' + str(len(adjacencies[1])))
    node_trace.text = node_text


    weightedEdges = []
    weights=[]
    for edge in G.edges:
        fNode = edge[0]
        lNode = edge[1]
        weight=int(random.randint(1,100))
        weightedEdges.append([fNode, lNode, weight])
        weights.append(weight)



    #Create adjacency matrix --- 0 = no edge
    #edgeMatrix holds the edge weights
    adjacencyMatrix=[[0 for n in G.nodes]for n in G.nodes]



    for n in weightedEdges:
        adjacencyMatrix [n[0]] [n[1]]= n[2]

    #Update Matrix for both directions. i.e. a value for node 1->5 and node 5->1
    j=0
    for node in adjacencyMatrix:
        for i in range(numNodes):
            if node[i]>0:
                adjacencyMatrix[i][j]=node[i]
        j=j+1

    #update weightedEdges for both directions
    j = 0
    for edge in G.edges:
        fNode = edge[0]
        lNode = edge[1]
        weightedEdges.append([lNode, fNode, weights[j]])
        j = j + 1


    eweights_trace = go.Scatter(x=xtext, y=ytext, mode='text',
                                marker_size=0.5,
                                text=weights,
                                textposition='top center',
                                hovertemplate='weight: %{text}<extra></extra>')


    # Create Network Graph
    fig = go.Figure(data=[edge_trace, node_trace,eweights_trace],
                    layout=go.Layout(
                        title='<br>Network graph',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        annotations=[dict(
                            text="",
                            showarrow=False,
                            xref="paper", yref="paper",
                            x=0.005, y=-0.002)],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )


    #fig.show()


    print("number of nodes: ", numNodes)
    print("number of edges: ", len(G.edges))


    return adjacencyMatrix, weightedEdges
