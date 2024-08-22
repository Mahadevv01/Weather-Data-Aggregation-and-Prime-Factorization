def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        exponent = 0
        while (n % i) == 0:
            n //= i
            exponent += 1
        if exponent > 0:
            factors.append((i, exponent))
        i += 1
    if n > 1:
        factors.append((n, 1))
    return factors
