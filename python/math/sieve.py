def sieve(n):
    primes = []
    minp = [0] * (n + 1)
    for i in range(2, n + 1):
        if minp[i] == 0:
            minp[i] = i
            primes.append(i)
        for p in primes:
            if i * p > n or p > minp[i]:
                break
            minp[i * p] = p
    return primes, minp

# leetcode 204. 计数质数
if __name__ == "__main__":
    n = int(input())
    primes, minp = sieve(n)
    print(bisect_left(primes, n))
    
