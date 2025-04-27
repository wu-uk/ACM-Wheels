#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pll = pair<ll, ll>;
using graph = vector<vector<pll>>;
constexpr ll INF = 1e18;

vector<ll> dijkstra(graph &g, ll s) {
    vector<ll> dist(g.size(), INF);
    priority_queue<pll, vector<pll>, greater<pll>> pq;
    dist[s] = 0;
    pq.emplace(0, s);
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (dist[u] < d) continue;
        for (auto [w, v] : g[u]) {
            if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                pq.emplace(dist[v], v);
            }
        }
    }
    return dist;
}

// luogu P4779 模板 单源最短路径（标准版）
int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    ll n, m, s;
    cin >> n >> m >> s;
    graph g(n + 1);
    for (int i = 0; i < m; ++i) {
        ll u, v, w;
        cin >> u >> v >> w;
        g[u].emplace_back(w, v);
    }
    auto dist = dijkstra(g, s);
    for (int i = 1; i <= n; ++i) {
        cout << dist[i] << " \n"[i == n];  
    }
}