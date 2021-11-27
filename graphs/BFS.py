class Graph:
    adj_list: dict = None

    def __init__(self):
        self.adj_list = {}

    def addEdge(self, a, b):
        if a not in self.adj_list:
            self.adj_list[a] = []
        self.adj_list[a].append(b)
        if b not in self.adj_list:
            self.adj_list[b] = []
        self.adj_list[b].append(a)


visited = []


def DFS(adj_list: dict, current_node: int):
    if current_node in visited:
        return
    visited.append(current_node)
    print(current_node)
    for node in adj_list[current_node]:
        DFS(adj_list, node)


queue: list = []
visited_bfs: list = []


def BFS(adj_list: dict, current_node: int):
    if current_node in visited_bfs:
        return
    visited_bfs.append(current_node)
    print(current_node)
    queue.append(current_node)
    while len(queue) > 0:
        node = queue.pop(0)
        for neighbour in adj_list[node]:
            if neighbour in visited_bfs:
                continue
            print(neighbour)
            queue.append(neighbour)
            visited_bfs.append(neighbour)


graph: Graph = Graph()
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 3)
graph.addEdge(2, 4)
graph.addEdge(3, 5)
graph.addEdge(3, 4)

DFS(graph.adj_list, 1)

print("-------------------------------------BFS----------------------------------------")

BFS(graph.adj_list, 1)
