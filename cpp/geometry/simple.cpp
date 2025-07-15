#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using db = double;

constexpr db eps = 1e-8;
constexpr db INF = 1e18;
constexpr db PI = acos(-1);

struct P {
    db x, y;
    P(db x = 0, db y = 0) : x(x), y(y) {}

    P operator+(const P &o) const { return P(x + o.x, y + o.y); }
    P operator-(const P &o) const { return P(x - o.x, y - o.y); }
    P operator*(const db &k) const { return P(x * k, y * k); }
    db operator*(const P &o) const { return x * o.x + y * o.y; }  // 点乘
    db operator^(const P &o) const { return x * o.y - y * o.x; }  // 叉乘

    bool operator<(const P &o) const {
        if (fabs(y - o.y) > eps) return y < o.y;
        return x < o.x;
    }
};

db abs2(const P &p) { return p * p; }
db abs(const P &p) { return sqrt(abs2(p)); }
db dist2(const P &a, const P &b) { return abs2(a - b); }
db dist(const P &a, const P &b) { return abs(a - b); }

int dir(const P &p, const P &a, const P &b) {  // 凸包专用
    db x = (a - p) ^ (b - p);                  // 叉乘
    if (x > eps) return 1;                     // counter-clockwise
    if (x < -eps) return -1;                   // clockwise
    return 0;                                  // in the same line
}

P rotate(const P &o, const P &p, db rad) {  // 点P绕点O逆时针旋转rad弧度
    P v = p - o;
    P w = P(sin(rad), cos(rad));
    return o + P(v ^ w, v * w);
}

struct L {
    P a, b, ab;
    L() {}
    L(P a, P b) : a(a), b(b), ab(b - a) {}

    bool operator/(const L &o) const { return abs(ab ^ o.ab) < eps; }                         // 平行
    bool operator-(const L &o) const { return (*this / o) && (a - o.a) * (o.b - o.a) == 0; }  // 共线
    bool operator|(const L &o) const { return abs(ab * o.ab) < eps; }                         // 垂直
};

P project(const P &p, const L &l) { return l.a + l.ab * (l.ab * (p - l.a) / dist2(l.a, l.b)); }
P reflect(const P &p, const L &l) { return project(p, l) * 2 - p; }

int pos(const P &p, const L &l) {
    db x = l.ab ^ (p - l.a);
    if (x > eps) return 1;    // 1: 在逆时针方向
    if (x < -eps) return -1;  // -1: 在顺时针方向
    db y = l.ab * (p - l.a);
    if (y < -eps) return -2;            // -2: 反向延长线
    if (y > dist2(l.a, l.b)) return 2;  // 2: 正向延长线
    return 0;                           // 0: 点在线段上
}

bool not_overlap(const L &u, const L &v) {
    auto [x1, x2] = minmax(u.a.x, u.b.x);
    auto [y1, y2] = minmax(u.a.y, u.b.y);
    auto [x3, x4] = minmax(v.a.x, v.b.x);
    auto [y3, y4] = minmax(v.a.y, v.b.y);
    return x1 > x4 || x2 < x3 || y1 > y4 || y2 < y3;
}
bool intersect(const L &u, const L &v) {
    if (not_overlap(u, v)) return false;
    return pos(u.a, v) * pos(u.b, v) <= 0 and pos(v.a, u) * pos(v.b, u) <= 0;
}

db distLP(const P &p, const L &l) { return abs(l.ab ^ (p - l.a)) / abs(l.ab); }
db distSP(const P &p, const L &l) { // 点到线段的距离
    if ((p - l.a) * l.ab < -eps) return dist(p, l.a);
    if ((p - l.b) * l.ab > eps) return dist(p, l.b);
    return distLP(p, l);
}
db distSS(const L &u, const L &v) { // 线段到线段的距离
    if (intersect(u, v)) return 0;
    return min({distSP(u.a, v), distSP(u.b, v), distSP(v.a, u), distSP(v.b, u)});
}

P cross(const L &u, const L & v) {
    db a = u.ab ^ v.ab;
    db b = u.ab ^ (u.b - v.a);
    if (abs(a) < eps and abs(b) < eps) return v.a;
    return v.a + v.ab * (b / a);
}

using Poly = vector<P>;

db area(const Poly &g) { // 0-based
    db res = 0;
    for (size_t i = 0; i < g.size(); i++) {
        res += g[i] ^ g[(i + 1) % g.size()];
    }
    return abs(res) / 2;
}

int contain(const Poly &g, const P &p) {
    bool inPoly = false;
    for (size_t i = 0; i < g.size(); i++) {
        P a = g[i] - p, b = g[(i + 1) % g.size()] - p;
        if (abs(a^b) < eps and a*b <= eps) return 0; // 0: 点在边上
        if (a.y > b.y) swap(a, b);
        if (a.y <= 0 and 0 < b.y and (a^b) > eps) inPoly = !inPoly;
    }
    return inPoly ? 1 : -1;
}

bool isConvex(const Poly &g) {
    int n = g.size();
    assert(n >= 3);
    bool flag[3] = {0};
    for (int i = 0; i < n; i++) 
        flag[dir(g[i], g[(i+1)%n], g[(i+2)%n]) + 1] = true;
    // return flag[0] ^ flag[2]; 直线不算凸包
    return !(flag[0] and flag[2]); // 直线算凸包
}

// 1. dir()改成<=可以去除边界上的点
// 2. 可以考虑使用unique去重
Poly convexHull(Poly &g) {
    sort(g.begin(), g.end());
    int n = g.size();
    Poly res(n * 2);
    int k = 0;
    for (int i = 0; i < n; i++) {
        while (k > 1 and dir(res[k-2], res[k-1], g[i]) < 0) k--;
        res[k++] = g[i];
    }
    for (int i = n-2, t = k; i >= 0; i--) {
        while (k > t and dir(res[k-2], res[k-1], g[i]) < 0) k--;
        res[k++] = g[i];
    }
    res.resize(k - 1);
    return res;
}

db diameter(const Poly &g) {
    db res = 0;
    size_t j = 0;
    for (auto p : g) {
        while (dist2(g[j], p) < dist2(g[(j+1)%g.size()], p))
            j = (j + 1) % g.size();
        res = max(res, dist(g[j], p));
    }
    return res;
}

// 射线切割凸包，得到左侧的半边
Poly convexCut(const Poly &p, L l) {
    Poly q;
    for (size_t i = 0; i < p.size(); i++) {
        P a = p[i], b = p[(i+1)%p.size()];
        if (pos(a, l) >= 0) q.push_back(a);
        if (pos(a, l) * pos(b, l) < 0) q.push_back(cross(L(a,b), l));
    }
    return q;
}

using pit = Poly::iterator;
void closest_pair(const pit l, const pit r, db &d) {
    if (r - l <= 1) return;
    Poly strip;
    pit m = l + (r - l) / 2;
    db mx = m->x;
    closest_pair(l, m, d), closest_pair(m, r, d);
    inplace_merge(l, m, r);
    for (pit i = l; i != r; ++i) if (abs(i->x - mx) * abs(i->x - mx) < d) strip.push_back(*i);
    for (pit i = strip.begin(), j = i; i != strip.end(); ++i) {
        while (j!= strip.end() and (j->y - i->y) * (j->y - i->y) < d) ++j;
        for (pit k = i + 1; k != j; ++k) d = min(d, dist2(*i, *k));
    }
}
bool sortX(const P &a, const P &b) { return a.x < b.x; }
db closePair(Poly p) {
    sort(p.begin(), p.end(), sortX);
    db d = INF;
    closest_pair(p.begin(), p.end(), d);
    return sqrt(d);
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    int n; cin >> n;
    Poly p(n);
    for (int i = 0; i < n; ++i) cin >> p[i].x >> p[i].y;
    db  ans = closePair(p);
    cout << fixed << setprecision(10) << ans << "\n";
}