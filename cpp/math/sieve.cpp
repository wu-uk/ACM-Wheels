#include <bits/stdc++.h>
using namespace std;

vector<int> minp, primes;
void sieve(int n) {
    minp.assign(n + 1, 0);
    primes.clear();
    for (int i = 2; i <= n; i++) {
        if (!minp[i]) primes.emplace_back(minp[i] = i);
        for (auto p : primes) {
            if (i * p > n or p > minp[i]) break;
            minp[i * p] = p;
        }
    }
}

vector<int> phi;
void getPhi(int n) {
    phi.assign(n + 1, 0);
    minp.assign(n + 1, 0);
    primes.clear();
    for (int i = 2; i <= n; i++) {
        if (!minp[i]) {
            primes.emplace_back(minp[i] = i);
            phi[i] = i - 1;
        }
        for (auto p : primes) {
            if (i * p > n or p > minp[i]) break;
            minp[i * p] = p;
            if (i % p == 0) {
                phi[i * p] = phi[i] * p;
            } else {
                phi[i * p] = phi[i] * (p - 1);
            }
        }
    }
}
// luogu P3383 【模板】线性筛素数
int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    int n, m;
    cin >> n >> m;
    sieve(n);
    for (int i = 0; i < m; ++i) {
        int x;
        cin >> x;
        cout << primes[x - 1] << "\n";
    }
}