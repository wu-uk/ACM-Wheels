class Trie:
    def __init__(self):
        self.children = dict()
        self.is_end = False
        self.word = 0
        self.count = 0
    
    def insert(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
            node.count += 1
        node.is_end = True
        node.word += 1
    
    def search(self, word):
        node = self
        for c in word:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.count
    
# luogu 8306 【模板】字典树
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, q = map(int, input().split())
        trie = Trie()
        for _ in range(n):
            s = input()
            trie.insert(s)
        for _ in range(q):
            s = input()
            print(trie.search(s))