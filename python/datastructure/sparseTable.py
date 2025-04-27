class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        k = n.bit_length()
        self.max = [[0] * n for _ in range(k)]
        for i in range(n):
            self.max[0][i] = arr[i]
        for j in range(1, k):
            for i in range(n - (1 << j) + 1):
                self.max[j][i] = max(self.max[j - 1][i], self.max[j - 1][i + (1 << (j - 1))])
    
    def query(self, l, r):
        k = (r - l + 1).bit_length() - 1
        return max(self.max[k][l], self.max[k][r - (1 << k) + 1])

# luogu 3865 【模板】ST表
if __name__ == "__main__":
    import sys
    input = lambda: sys.stdin.readline().rstrip('\n')
    print = lambda x: sys.stdout.write(str(x) + '\n')
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    st = SparseTable(a)
    for _ in range(m):
        l, r = map(int, input().split())
        print(st.query(l - 1, r - 1))
    