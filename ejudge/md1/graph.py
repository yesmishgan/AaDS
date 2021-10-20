import sys
from collections import deque

def bfs(start_vertex, edges):

    q = deque()
    vertices_done = {start_vertex}
    q.append(start_vertex)

    if start_vertex not in edges.keys():
        print(start_vertex)
        return

    while len(q) != 0:
        vertex = q.popleft()
        print(vertex)
        if vertex not in edges.keys():
            continue
        for v in edges[vertex]:
            if v not in vertices_done:
                vertices_done.add(v)
                q.append(v)

def dfs(start_vertex, edges):

    q = deque()
    vertices_done = {start_vertex}
    q.append(start_vertex)
    if start_vertex not in edges.keys():
        print(start_vertex)
        return
    q.extend(edges[start_vertex])
    print(start_vertex)
    
    neighboor = deque()

    while len(q) != 0:
        vertex = q.popleft()
        while vertex in vertices_done and len(q) > 0:
            vertex = q.popleft()
        if vertex not in vertices_done:
            vertices_done.add(vertex)
            print(vertex)
        if vertex in edges.keys():
            for elem in edges[vertex]:
                if elem in vertices_done:
                    pass
                elif elem in q:
                    q.remove(elem)
                    neighboor.append(elem)
                else:
                    neighboor.append(elem)

        neighboor.reverse()
        q.extendleft(neighboor)
        neighboor.clear()

if __name__=="__main__":

    data = sys.stdin.readline().split()
    graph_type = data[0]
    start_vertex = data[1]
    search_type = data[2]
    edges = dict()

    for line in sys.stdin:
        data = line.split()
        if len(data) != 2:
            continue

        key = data[0]

        if data[0] not in edges:
            edges[key] = []
        edges[key].append(data[1])

        if graph_type == 'u':
            if data[1] not in edges:
                edges[data[1]] = []
            edges[data[1]].append(key)
    

    for key in edges:
        edges[key].sort()
    
    if search_type == 'b':
        bfs(start_vertex, edges)
    elif search_type == 'd':
        dfs(start_vertex, edges)
