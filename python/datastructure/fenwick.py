class fenwick:
    # 单点修改，区间查询
    def __init__(self, a):
        self.n = len(a) - 1 
        self.tree = [0] * (n + 1)
        for i in range(1, self.n + 1):
            self.update(i, a[i])

    def lowbit(self, x):
        return x & -x

    def update(self, x, v):
        while x <= self.n:
            self.tree[x] += v
            x += self.lowbit(x)
        
    def prefix_sum(self, x):
        res = 0
        while x > 0:
            res += self.tree[x]
            x -= self.lowbit(x)
        return res
    
    def query(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

# luogu 3374 树状数组 1
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    fw = fenwick(a)
    for _ in range(m):
        op, *args = map(int, input().split())
        if op == 1:
            x, v = args
            fw.update(x, v)
        else:
            l, r = args
            print(fw.query(l, r))