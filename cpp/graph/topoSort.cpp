#include <bits/stdc++.h>
using namespace std;
using graph = vector<vector<int>>;
vector<int> topoSort(graph &g, vector<int> indeg) {
    queue<int> q;
    for (size_t i = 0; i < indeg.size(); ++i) {
        if (indeg[i] == 0) q.push(i);
    }
    vector<int> res;
    res.reserve(g.size());
    while (!q.empty()) {
        int u = q.front();
        res.emplace_back(u);
        q.pop();
        for (int v : g[u]) {
            indeg[v]--;
            if (indeg[v] == 0) {
                q.push(v);
            }
        }
    }
    assert(res.size() == g.size());
    return res;
}