# Написать функцию, принимающую на вход строку из последовательности круглых, квадратных, фигурных и треугольных скобок.
# и возвращающую True если последовательность верна и False - если нет.

def check_brackets(line: str):
    banka = []
    for i in range(len(line)):
        b = line[i]
        if b in '( [ { <'.split(' '):
            banka.append(b)
        else:
            if not len(banka):
                return False
            if b == ')' and banka[-1] == '(':
                banka.pop(-1)
            elif b == '}' and banka[-1] == '{':
                banka.pop(-1)
            elif b == ']' and banka[-1] == '[':
                banka.pop(-1)
            elif b == '>' and banka[-1] == '<':
                banka.pop(-1)
            else:
                return False
    return not banka


if __name__ == '__main__':
    # Simple tests:
    print(check_brackets('(((){[]})<>)'))  # True
    print(check_brackets('((()<{()}>)())'))  # True
    print(check_brackets('(((<){}(>)[]))'))  # False
    print(check_brackets('{<>(<[]>())}'))  # True
