# Написать функцию, генерирующую ровно 1<k<40 простых чисел и возвращающую их упорядоченный список.
# Тело функции должно быть в 1 строку. k всегда в указанном диапазоне и всегда int.

def generate_primes(n):
    return [x**2+x+41 for x in range(n)]


if __name__ == '__main__':
    # Simple tests:
    print(generate_primes(4))  # [2,3,5,7]
    print(generate_primes(8))  # [2,3,5,7,11,13,17,19]