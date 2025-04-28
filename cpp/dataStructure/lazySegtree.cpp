#include <bits/stdc++.h>
using namespace std;
using ll = long long;

template <typename S, typename F, typename Op>
class LazySegTree {
private:
    int n;
    vector<S> data;
    vector<F> lazy;
    vector<bool> pending;
    int left(int u) const { return 2*u + 1; }
    int right(int u) const { return 2*u + 2; }
    bool inRange(int l, int r, int L, int R) const { return L <= l and r <= R; }
    bool outRange(int l, int r, int L, int R) const { return r < L or R < l; }
    void build(int u, int l, int r, const vector<S> &v) {
        if (l == r) {
            data[u] = v[l];
        } else {
            int m = (l + r) / 2;
            build(left(u), l, m, v);
            build(right(u), m + 1, r, v);
            data[u] = Op::op(data[left(u)], data[right(u)]);
        }
    }
    void apply(int u, const F &f) { // 打tag
        data[u] = Op::mapping(f, data[u]);
        if (left(u) < 4 * n) {
            lazy[u] = Op::composition(f, lazy[u]);
            pending[u] = true;
        }
    }
    void pushdown(int u) { // 下推tag
        if (pending[u]) {
            apply(left(u), lazy[u]);
            apply(right(u), lazy[u]);
            lazy[u] = Op::id();
            pending[u] = false;
        }
    }
    void update(int u, int l, int r, int L, int R, const F &f) {
        if (outRange(l, r, L, R)) return;
        if (inRange(l, r, L, R)) {
            apply(u, f);
        } else {
            pushdown(u);
            int m = (l + r) / 2;
            update(left(u), l, m, L, R, f);
            update(right(u), m + 1, r, L, R, f);
            data[u] = Op::op(data[left(u)], data[right(u)]);
        }
    }
    S query(int u, int l, int r, int L, int R) {
        if (outRange(l, r, L, R)) return Op::e();
        if (inRange(l, r, L, R)) return data[u];
        pushdown(u);
        int m = (l + r) / 2;
        return Op::op(query(left(u), l, m, L, R), query(right(u), m + 1, r, L, R));
    }
public:
    LazySegTree(const vector<S> &v) {
        n = (int)v.size();
        data.resize(4*n, Op::e());
        lazy.resize(4*n, Op::id());
        pending.resize(4*n, false);
        build(0, 0, n - 1, v);
    }
    void range_apply(int l, int r, const F &f) { update(0, 0, n - 1, l, r, f); }
    S range_query(int l, int r) { return query(0, 0, n - 1, l, r); }
};

struct Info {
    ll sum;
    int size;
    Info(ll sum = 0, int size = 0) : sum(sum), size(size) {}
};

struct Tag {
    ll add;
    Tag(ll add = 0) : add(add) {}
};

struct Op {
    // 合并区间信息
    static Info op(const Info &l, const Info &r) {
        return Info(l.sum + r.sum, l.size + r.size);
    }
    // 区间信息单位元
    static Info e() {
        return Info(0, 0);
    }
    // 映射tag到区间信息
    static Info mapping(const Tag &t, const Info &x) {
        return Info(x.sum + t.add * x.size, x.size);
    }
    // 合并tag
    static Tag composition(const Tag &f, const Tag &g) {
        return Tag(f.add + g.add);
    }
    // tag单位元
    static Tag id() {
        return Tag(0);
    }
};

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);
    int n, q; cin >> n >> q;
    vector<ll> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    vector<Info> leaves(n);
    for (int i = 0; i < n; i++) {
        leaves[i] = Info(a[i], 1);
    }
    LazySegTree<Info, Tag, Op> seg(leaves);
    while (q--) {
        int op, l, r; cin >> op >> l >> r;
        l--; r--;
        if (op == 1) {
            ll x; cin >> x;
            seg.range_apply(l, r, Tag(x));
        } else {
            cout << seg.range_query(l, r).sum << endl; // print the sum of the range [l, r]
        }
    }
}