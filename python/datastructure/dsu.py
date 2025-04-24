class DSU:
    def __init__(self, n):
        """
        par[i] 表示节点 i 的父节点。
        siz[i] 表示以节点 i 为根的子树的大小。
        """
        self.par = list(range(n))
        self.siz = [1] * n

    def find(self, x):
        """
        查找节点 x 的根节点。
        """
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        """
        合并节点 x 和节点 y 的根节点。
        """
        x = self.find(x)
        y = self.find(y)
        if x == y: return False
        if self.siz[x] < self.siz[y]:
            x, y = y, x
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True
    
# luogu 1551 亲戚
if __name__ == "__main__":
    n, m, p = map(int, input().split())
    dsu = DSU(n+1)
    for _ in range(m):
        u, v = map(int, input().split())
        dsu.union(u, v)
    for _ in range(p):
        u, v = map(int, input().split())
        if dsu.find(u) == dsu.find(v):
            print("Yes")
        else:
            print("No")