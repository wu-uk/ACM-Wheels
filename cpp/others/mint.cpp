#include <bits/stdc++.h>
using namespace std;
using ll = long long;
template<ll MOD>
struct ModInt {
    ll x;
    ModInt(ll x = 0) : x((x % MOD + MOD) % MOD) {}
    
    ModInt operator+(ModInt o) const { return ModInt(x + o.x); }
    ModInt operator-(ModInt o) const { return ModInt(x - o.x); }
    ModInt operator*(ModInt o) const { return ModInt(x * o.x); }
    
    ModInt pow(ll e) const {
        ModInt res = 1, b = *this;
        for (; e; e >>= 1, b = b * b)
            if (e & 1) res = res * b;
        return res;
    }
    
    ModInt inv() const { return pow(MOD - 2); }
    ModInt operator/(ModInt o) const { return *this * o.inv(); }
    
    explicit operator int() const { return x; }
    friend ostream& operator<<(ostream& os, ModInt m) { return os << m.x; }
};
constexpr ll MM = 1e9+7;
using mint = ModInt<MM>;
// 使用时，常量要用mint()包裹，其余都当成普通int