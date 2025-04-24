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

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    primes, minp = sieve(n)
    print("Primes up to", n, ":", primes)
    print("Minimum prime factor for each number up to", n, ":", minp)
