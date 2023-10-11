# Написать функцию, генерирующую ровно 1<k<40 простых чисел и возвращающую их упорядоченный список.

def generate_primes(n):
    if type(n) == int:
        a = [0]*1000
        b = []

        for i in range(2, 1000):
            if a[i] == 0:
                b.append(i)
                if len(b) == n:
                    return b
                if i * i < 1000:
                    for j in range(i * i, 1000, i):
                        a[j] = 1
    else:
        return


if __name__ == '__main__':
    # Simple tests:
    print(generate_primes(4))  # [2,3,5,7]
    print(generate_primes(8))  # [2,3,5,7,11,13,17,19]
    print(generate_primes(-1))  # None
    print(generate_primes(3.5))  # None
