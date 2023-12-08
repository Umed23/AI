from collections import deque
print("UMED LADUNATH JOGI 104")
def bfs(graph, start):
   visited = set()
   queue = deque([start])
   while queue:
      vertex = queue.popleft()
      if vertex not in visited:
          visited.add(vertex)
          print(vertex)
          neighbors = graph[vertex]
          for neighbor in neighbors:
             if neighbor not in visited:
                   queue.append(neighbor)
# Example usage
graph = {
'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A', 'F'],
'D': ['B'],
'E': ['B', 'F'],
'F': ['C', 'E']
}
start_vertex = 'A'
visited_node = bfs(graph, start_vertex)
