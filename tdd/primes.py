def generate_prime_factors(n):
    factors = []
    i = 2
    while n != 1:
        while n % i == 0:
            factors.append(i)
            n /= i
        i += 1
    return tuple(factors)
