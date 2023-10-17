# Написать функцию, принимающую на вход число 3<n<1000 и возвращающее все простые числа из диапазона [1,n].
from math import sqrt


def filter_primes(n):
    if not (3 < n < 1000):
        return None
    primes = list(range(2, int(n) + 1)) #O(log(n))
    for divider in primes[:int(sqrt(n + 1))]:
        for j, num in enumerate(primes):
            if num % divider == 0 and num != divider:
                primes.pop(j)

    # for i in range(2, int(n) + 1): # O(n**2)
    #     num_divs = 0
    #     for j in range(2, i):
    #         if i % j == 0:
    #             num_divs += 1
    #     if not num_divs:
    #         primes.append(i)
    return primes


if __name__ == '__main__':
    # Simple tests:
    print(filter_primes(4))  # [2,3]
    print(filter_primes(10))  # [2,3,5,7]
    print(filter_primes(100))  # None
    # print(filter_primes(3.5))  # [2,3]
