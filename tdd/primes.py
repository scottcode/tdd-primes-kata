def generate_prime_factors(n):
    primes = [1]
    if n % 2 == 0:
        primes.append(2)
        n /= 2
    if n > 1:
        primes.append(n)
    return tuple(primes)