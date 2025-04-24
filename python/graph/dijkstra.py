from queue import PriorityQueue
def dijkstra(graph, start):
    """
    graph: 图的邻接表，元素为 (权重, 邻节点) 元组列表。
    start: 起始节点编号。
    返回各节点最短路径长度列表，无法到达则为 1e18。
    """
    dist = [1e18] * len(graph)
    dist[start] = 0
    q = PriorityQueue()
    q.put((0, start))
    while not q.empty():
        d, u = q.get()
        if d > dist[u]:
            continue
        for w, v in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                q.put((dist[v], v))
    return dist

if __name__ == "__main__":
    n, m, s = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))

    dist = dijkstra(graph, s)
    print(*dist[1:])
    
    
        