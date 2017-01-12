def generate_prime_factors(n):
    factors = []
    primes = []
    i = 2
    while n != 1:
        if any(i % p == 0 for p in primes):
            i += 1
            continue
        primes.append(i)
        while n % i == 0:
            factors.append(i)
            n /= i
        i += 1
    return tuple(factors)
