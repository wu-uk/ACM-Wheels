#include <bits/stdc++.h>
using namespace std;

using i128 = __int128;

ostream& operator<<(ostream& os, i128 x) {
    if (x < 0) {
        os << "-";
        x = -x;
    }
    if (x == 0) return os << 0;
    string s;
    while (x) {
        s += char('0' + x % 10);
        x /= 10;
    }
    reverse(s.begin(), s.end());
    return os << s;
}

istream& operator>>(istream& is, i128& x) {
    string s; is >> s;
    x = 0;
    for (auto c : s) {
        x = x * 10 + c - '0';
    }
    return is;
}

i128 sqrti128(i128 x) {
    i128 lo = 0, hi = 1e18;
    while (lo < hi) {
        i128 mid = (lo + hi + 1) / 2;
        if (mid * mid <= x) {
            lo = mid;
        } else {
            hi = mid - 1;
        }
    }
    return lo;
}


int main() {
    i128 a = 1e18;
    a = a * a;
    cout << sqrti128(a) << "\n";
    return 0;
}