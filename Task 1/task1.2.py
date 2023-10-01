# Написать функцию, генерирующую ровно 1<k<40 простых чисел и возвращающую их упорядоченный список.

from FuncST import filter_primes


def generate_primes(n):
    if (type(n) == int) and (1 < n < 40):
        c = filter_primes(200)
        return c[:n]
    else:
        return None


if __name__ == '__main__':
    # Simple tests:
    print(generate_primes(4))  # [2,3,5,7]
    print(generate_primes(8))  # [2,3,5,7,11,13,17,19]
    print(generate_primes(-1))  # None
    print(generate_primes(3.5))  # None
