import queue
def toposort(n, indeg, graph):
    """
    n: 节点数
    indeg: 入度列表
    graph: 图的邻接表
    返回拓扑排序结果，若有环则返回空列表
    """
    q = queue.Queue()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.put(i)
    ans = []    
    while not q.empty():
        u = q.get()
        ans.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.put(v)
    if len(ans) < n:
        return []
    return ans

# luogu 3644 拓扑排序
if __name__ == "__main__":
    n = int(input())
    indeg = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for u in range(n):
        graph[u+1] = list(map(int, input().split()))[:-1]
        for v in graph[u+1]:
            indeg[v] += 1
    ans = toposort(n, indeg, graph)
    print(*ans)