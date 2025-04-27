#include <bits/stdc++.h>
using namespace std;

vector<int> minp, primes;
void sieve(int n) {
    minp.assign(n + 1, 0);
    primes.clear();
    for (int i = 2; i <= n; i++) {
        if (minp[i] == 0) primes.emplace_back(minp[i] = i);
        for (auto p : primes) {
            if (i * p > n or p > minp[i]) break;
            minp[i * p] = p;
        }
    }
}

// luogu P3383 【模板】线性筛素数
int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    int n, m; cin >> n >> m;
    sieve(n);
    for (int i = 0; i < m; ++i) {
        int x; cin >> x;
        cout << primes[x - 1] << "\n";
    }
}