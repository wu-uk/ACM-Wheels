def get_border(s):
    n = len(s)
    border = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = border[j - 1]
        if s[i] == s[j]:
            j += 1
        border[i] = j
    return border

def kmp(s, t):
    n, m = len(s), len(t)
    ans = []
    border = get_border(t)
    j = 0
    for i in range(n):
        while j > 0 and s[i] != t[j]:
            j = border[j - 1]
        if s[i] == t[j]:
            j += 1
        if j == m:
            ans.append(i - m + 1)
            j = border[j - 1]
    return ans, border

# luogu 3375 【模板】KMP字符串匹配
if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    ans, border = kmp(s, t)
    for i in ans: print(i+1)
    print(*border)