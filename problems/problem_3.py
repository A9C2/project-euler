import math

n = 600_851_475_143

def trial_division(n):
    if n < 2:
        return False
    a = 2
    while a <= math.sqrt(n):
        if n % a == 0:
            return False
        a += 1
    return True

def prime_factorization(n):
    prime_factors = []
    while not trial_division(n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                prime_factors.append(i)
                n = int(n / i)
                break
    prime_factors.append(n)
    return prime_factors

print(prime_factorization(n)[-1])

    