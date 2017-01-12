def generate_prime_factors(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n /= 2
    while n % 3 == 0:
        primes.append(3)
        n /= 3
    while n % 5 == 0:
        primes.append(5)
        n /= 5
    if n > 1:
        primes.append(n)
    return tuple(primes)
