def sieve_of_eratosthenes(n):

    prime_flags = [True] * (n+1)

    p = 2

    while p*p <= n:
        if prime_flags[p]:
            for i in range(p*p, n+1, p):
                prime_flags[i] = False
        p += 1

    primes = []
    for i in range(2, n+1):
        if prime_flags[i]:
            primes.append(i)

    return primes
