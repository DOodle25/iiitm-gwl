import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def prim(self):
        mst = []
        visited = [False] * self.V
        min_heap = [(0, 0, -1)]  # (weight, vertex, predecessor)
        while min_heap and len(mst) < self.V:
            weight, u, pred = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            if pred != -1:
                mst.append((pred, u, weight))
            for v, w in self.get_adjacent(u):
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v, u))
        return mst

    def get_adjacent(self, u):
        adj = []
        for edge in self.edges:
            if edge[0] == u:
                adj.append((edge[1], edge[2]))
            elif edge[1] == u:
                adj.append((edge[0], edge[2]))
        return adj

    def kruskal(self):
        parent = [i for i in range(self.V)]
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        def union(u, v):
            parent[find(u)] = find(v)
        mst = []
        self.edges.sort(key=lambda x: x[2])
        for u, v, w in self.edges:
            if find(u) != find(v):
                mst.append((u, v, w))
                union(u, v)
        return mst

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        pred = [None] * self.V
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in self.get_adjacent(u):
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    heapq.heappush(heap, (dist[v], v))
        return dist, pred

    def bellman_ford(self, src):
        dist = [float('inf')] * self.V
        pred = [None] * self.V
        dist[src] = 0
        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    pred[v] = u
                if dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w
                    pred[u] = v
        # Check for negative cycles
        for u, v, w in self.edges:
            if dist[u] + w < dist[v]:
                raise ValueError("Graph contains negative weight cycle")
        return dist, pred

    def get_path(self, pred, target):
        path = []
        while target is not None:
            path.append(target)
            target = pred[target]
        return path[::-1]

# Example usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)
print("Prim's MST:", g.prim())
print("Kruskal's MST:", g.kruskal())
dist, pred = g.dijkstra(0)
print("Dijkstra distances:", dist)
print("Dijkstra path to 4:", g.get_path(pred, 4))
dist, pred = g.bellman_ford(0)
print("Bellman-Ford distances:", dist)
print("Bellman-Ford path to 4:", g.get_path(pred, 4))