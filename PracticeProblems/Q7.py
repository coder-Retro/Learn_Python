def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

primes = list(filter(is_prime,range(1,31)))
print(f"Primes: {primes}")