#dfs
print('DFS')
graph = {
    "A":["B", "C"],
    "B":["D", "E"],
    "C":["F"],
    "D":[],
    "E":[],
    "F":[]
}

visited = set()

def DFS(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for child in graph[node]:
            DFS(visited, graph, child)
DFS(visited, graph, "A")

print('BFS')
#bfs
from collections import deque
def BFS(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
        queue.extend(graph[node])
BFS(graph,"A")