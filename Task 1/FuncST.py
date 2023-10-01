def filter_primes(n):
    c = []
    if n >= 2:
        for i in range(2,  int(n)+1):
            k = 0
            for l in range(1, i+1):
                if i % l == 0:
                    k = k+1
            if k == 2:
                c.append(i)
        return (c)
    else:
        return None


def generate_primes(n):
    if (type(n) == int) and (1 < n < 40):
        c = filter_primes(200)
        # print(len(c))
        return c[:n]
    else:
        return None
