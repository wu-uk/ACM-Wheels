#include <bits/stdc++.h>
using namespace std;

struct ST {
    vector<vector<int>> st;
    ST (const vector<int>& arr) {
        int n = arr.size();
        st.assign(__lg(n) + 1, vector<int>(n)); // 维度小的放前面
        for (int i = 0; i < n; ++i) st[0][i] = arr[i];
        for (int j = 1; 1 << j <= n; ++j) {
            for (int i = 0; i + (1 << j) <= n; ++i) {
                st[j][i] = max(st[j - 1][i], st[j - 1][i + (1 << (j - 1))]);
            }
        }
    }
    int query(int l, int r) { // [l, r]
        int k = __lg(r - l + 1);
        return max(st[k][l], st[k][r - (1 << k) + 1]);
    }
};

// luogu P3865 【模板】ST 表
int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    int n, m; cin >> n >> m;
    vector<int> arr(n + 1);
    for (int i = 1; i <= n; ++i) cin >> arr[i];
    ST st(arr);
    for (int i = 0; i < m; ++i) {
        int l, r; cin >> l >> r;
        cout << st.query(l, r) << "\n";
    }
}