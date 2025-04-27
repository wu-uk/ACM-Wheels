#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> f, sz;
    DSU(int n) : f(n + 1), sz(n + 1, 1) { iota(f.begin(), f.end(), 0); }
    int find(int x) { return f[x] == x ? x : f[x] = find(f[x]); }
    bool merge(int x, int y) {
        x = find(x), y = find(y);
        if (x == y) return false;
        if (sz[x] < sz[y]) swap(x, y);
        sz[x] += sz[y];
        f[y] = x;
        return true;
    }
};

// luogu 1551 亲戚
int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    int n, m, p; cin >> n >> m >> p;
    DSU dsu(n);
    for (int i = 0; i < m; ++i) {
        int x, y; cin >> x >> y;
        dsu.merge(x, y);
    }
    for (int i = 0; i < p; ++i) {
        int x, y; cin >> x >> y;
        cout << (dsu.find(x) == dsu.find(y)? "Yes" : "No") << "\n";
    }
}