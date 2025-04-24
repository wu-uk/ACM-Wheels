class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        self.max = [[0] * (n.bit_length()) for _ in range(n)]
        for i in range(n):
            self.max[i][0] = arr[i]
        for j in range(1, n.bit_length()):
            for i in range(n - (1 << j) + 1):
                self.max[i][j] = max(self.max[i][j - 1], self.max[i + (1 << (j - 1))][j - 1])
    
    def query(self, l, r):
        k = (r - l + 1).bit_length() - 1
        return max(self.max[l][k], self.max[r - (1 << k) + 1][k])

# luogu 3865 【模板】ST表
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    st = SparseTable(a)
    for _ in range(m):
        l, r = map(int, input().split())
        print(st.query(l, r))
    