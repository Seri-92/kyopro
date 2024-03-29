from heapq import heappop, heappush


def dijkstra(graph, start):
    """ 
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
    """
    n = len(graph)
    dist, parents = [float("inf")] * n, [-1] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))

    return dist, parents


V, E, r = map(int, input().split())
G = [[] for _ in range(V)]
for _ in range(E):
    s, t, d = map(int, input().split())
    G[s].append((t, d))

dist, parents = dijkstra(G, r)

for x in dist:
    if x == float('inf'):
        print('INF')
    else:
        print(x)
