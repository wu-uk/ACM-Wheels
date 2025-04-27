class Node:
    def __init__(self):
        self.to = []
        self.father = None
        self.hson = None
        self.top = None
        self.deep = 0
        self.size = 0
        self.dfn = 0
        self.id = 0

class TreeDivision:
    def __init__(self, n):
        self.n = n
        self.tot = 0
        self.tree = [Node() for _ in range(n + 1)]
        for i in range(1, n + 1): self.tree[i].id = i
        self.old_id = [0] * (n + 1)
        self.new_id = [0] * (n + 1)
    
    def add_edge(self, u, v):
        self.tree[u].to.append(v)
        self.tree[v].to.append(u)
    
    def _build(self, uid = None, fa = None, dep=0):
        if uid is None: return 0
        u = self.tree[uid]
        u.hson = None
        u.father = fa 
        u.deep = dep
        u.size = 1
        for vid in u.to:
            if vid == u.father: continue
            v = self.tree[vid]
            u.size += self._build(vid, uid, dep + 1)
            if u.hson is None or v.size > u.hson.size:
                u.hson = v
        return u.size
    
    def _decomposition(self, uid = None, top = None):
        u = self.tree[uid]
        u.top = top
        self.tot += 1
        u.dfn = self.tot
        self.old_id[u.dfn] = u.id
        self.new_id[u.id] = u.dfn
        if u.hson is not None:
            self._decomposition(u.hson, top)
            for vid in u.to:
                if vid == u.father or vid == u.hson: continue
                self._decomposition(vid, vid)
    
    def build(self, root = 1):
        self._build(root, 0)
        self._decomposition(root, root)

    def lca(self, uid, vid):
        u = self.tree[uid]
        v = self.tree[vid]
        while u.top != v.top:
            if u.top is None or v.top is None: break
            if u.top.deep > v.top.deep: u = self.tree[u.top.father.id]  # 修正为self.tree
            else: v = self.tree[v.top.father.id]  # 修正为self.tree
        return u.id if u.deep < v.deep else v.id

# luogu 3379 【模板】最近公共祖先（LCA）
# TODO: 现在无法通过luogu 3379，会RE
from sys import stdin
input = lambda: stdin.readline().rstrip()
if __name__ == "__main__":
    n, m, s = map(int, input().split())
    tree = TreeDivision(n)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree.add_edge(u, v)
    tree.build(s)
    for _ in range(m):
        u, v = map(int, input().split())
        print(tree.lca(u, v))

    

            
        
        
        