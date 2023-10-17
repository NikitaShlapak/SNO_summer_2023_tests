# Написать функцию, генерирующую ровно 1<k<40 простых чисел и возвращающую их упорядоченный список.
from math import sqrt


def filter_primes(n):
    primes = list(range(2, int(n) + 1))
    for divider in primes[:int(sqrt(n + 1))]:
        for j, num in enumerate(primes):
            if num % divider == 0 and num != divider:
                primes.pop(j)
    return primes


def generate_primes(n):
    if (not (3 < n < 1000)) or (n - int(n)):
        return None
    primes = filter_primes(1000)
    return primes[:n]


if __name__ == '__main__':
    # Simple tests:
    print(generate_primes(4))  # [2,3,5,7]
    print(generate_primes(8))  # [2,3,5,7,11,13,17,19]
    print(generate_primes(-1))  # None
    print(generate_primes(3.5))  # None
