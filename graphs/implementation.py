from collections import defaultdict

graph = defaultdict(list)

def addEdge(graph: defaultdict, u, v):
    graph[u].append(v)

def printEdge(graph: defaultdict):
    edge = []
    for node in graph:
        for adj in graph[node]:
            edge.append((node, adj))
    return edge

# declaration of graph as dictionary
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')

print(printEdge(graph))
