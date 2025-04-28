#include <bits/stdc++.h>
using namespace std;

struct Matrix {
    int n, m;
    vector<vector<int>> a;
    Matrix(int n, int m) : n(n), m(m), a(n + 1, vector<int>(m + 1)) {}
    Matrix(int n, int m, vector<vector<int>> a) : n(n), m(m), a(a) {}
    Matrix operator+(const Matrix &b) const {
        Matrix c(n, m);
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                c.a[i][j] = a[i][j] + b.a[i][j];
            }
        }
        return c;
    }
    Matrix operator*(const Matrix &b) const {
        Matrix c(n, b.m);
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= b.m; ++j) {
                for (int k = 1; k <= m; ++k) {
                    c.a[i][j] += a[i][k] * b.a[k][j];
                }
            }
        }
        return c;
    }
};