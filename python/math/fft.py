from cmath import exp, pi
def fft(x, inv=False):
    n = len(x)
    if n == 1: return x
    even = fft(x[0::2], inv)
    odd = fft(x[1::2], inv)
    y = [0] * n
    w, wn = 1, exp(2 * pi * (-1j if inv else 1j) / n)
    for i in range(n // 2):
        y[i] = even[i] + w * odd[i]
        y[i + n // 2] = even[i] - w * odd[i]
        w *= wn
    if inv:
        for i in range(n): y[i] /= 2
    return y
    
def poly_mul(a, b):
    n = len(a) + len(b) - 1
    m = 1 << n.bit_length()
    a += [0] * (m - len(a))
    b += [0] * (m - len(b))
    a = fft(a)
    b = fft(b)
    c = [a[i] * b[i] for i in range(m)]
    c = fft(c, inv=True)
    return [int(x.real + 0.5) for x in c][:n]

# luogu 3803 【模板】多项式乘法（FFT）
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = poly_mul(a, b)
    print(*c)