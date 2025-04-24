class TrieNode:
    def __init__(self):
        self.children = dict() # 子节点
        self.is_end = False # 是否为单词结尾
        self.word = 0 # 以当前节点为结尾的单词数
        self.count = 0 # 当前节点作为前缀的单词数
        
class Trie:
    def __init__(self):
        self.node = TrieNode()
    
    def insert(self, word):
        node = self.node
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.count += 1
        node.is_end = True
        node.word += 1
    
    def search(self, word):
        node = self.node
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