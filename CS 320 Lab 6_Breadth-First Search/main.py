from edgegraph import *
from collections import deque


def bfs(graph: GraphEL, start: VertexEL) -> list:
    
    if graph is None: 
        return []
    
    if start is None: 
        return []
    
    if start not in graph.vertices(): 
        return [] 
    
    visited = set()  
    bfs_order = []   
    queue = deque([start]) 

    while queue:
        current_vertex = queue.popleft()
        current_vertex_name = current_vertex.name
        if current_vertex_name not in visited:
            visited.add(current_vertex_name)
            bfs_order.append(current_vertex)
            adjacent_vertices = graph.adjacent_vertices(current_vertex)
            for vertex in adjacent_vertices:
                vertex_name = vertex.name
                if vertex_name not in visited:
                    queue.append(vertex)

    return bfs_order


if __name__ == "__main__":

    graph = parse_graph_file("graph.txt")
    start_vertex = graph.vertices()[0]
    bfs_result = bfs(graph, start_vertex)
    print("BFS Order:", bfs_result)
