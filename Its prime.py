def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(lst):
    return [x for x in lst if is_prime(x)]

lst = [10, 15, 3, 7, 11, 12, 13]
primes = find_primes(lst)
print("Prime Numbers:", primes)
