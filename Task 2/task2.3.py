# Написать функцию, принимающую на вход строку из последовательности круглых, квадратных, фигурных и треугольных скобок.
# и возвращающую True если последовательность верна и False - если нет.

def check_brackets(line: str):
    i = 0
    l = len(line)
    r = '{}[]<>'
    for j in range(len(r)):
        if j % 2 == 0:
            line = line.replace(r[j], '(')
        else:
            line = line.replace(r[j], ')')

    if len(line) > 1:
        while len(line) > 1 and i < l:
            line = ''.join(line.split('()'))
            i += 1

        if len(line) > 0:
            return False
        else:
            return True

    else:
        return False



if __name__ == '__main__':
    # Simple tests:
    print(check_brackets('(((){[]})<>)'))  # True
    print(check_brackets('((()<{()}>)())'))  # True
    print(check_brackets('(((<){}(>)[]))'))  # False
    print(check_brackets('{<>(<[]>())}'))  # True
