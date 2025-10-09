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

def findPath(graph, start, end, path=[]):
    '''
    It will give a error output as it will use a single list for the whole recursion stack for path
    Use debugger for reference
    '''
    path += [start] #uses same list throughout the recursion so wrong output
    #print(path)
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            new_node = findPath(graph, node, end,path)
            if new_node:
                return new_node

def find_path(graph, start, end, path=[]):
    path = path + [start]
    #print(path)
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath



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

#print(printEdge(graph))
print(findPath(graph, 'a','b'))
print(find_path(graph, 'a','b'))
