#include <bits/stdc++.h>
using namespace std;

int manacher(string &s) {
    // 计算字符串s的最长回文子串长度
    string t = "$#";
    for (auto c : s) {
        t += c;
        t += "#";
    }
    t += "!";
    int n = (int)t.size();
    vector<int> p(n, 0);
    int c = 0, r = 0; // c为当前中心，r为当前中心的最右边界
    for (int i = 1; i < n - 1; ++i) {
        if (i <= r) p[i] = min(r - i, p[2*c - i]);
        while (t[i - p[i] - 1] == t[i + p[i] + 1]) p[i]++;
        if (i + p[i] > r) {
            r = i + p[i];
            c = i;
        }
    }
    return *max_element(p.begin(), p.end());
}

// luogu 3805 【模板】manacher算法
int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    string s; cin >> s;
    cout << manacher(s) << "\n";
}