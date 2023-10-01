# Написать функцию, принимающую на вход строку из последовательности круглых скобок
# и возвращающую True если последовательность верна и False - если нет.
# Реализовать это так, чтобы сложность была не больше О(n).

def check_brackets(line: str):
    c = 0
    for i in range(len(line)):
        if line[i] == '(':
            c = c+1
        if line[i] == ')':
            c = c-1
    if len(line) == 0:
        return (False)
    if c == 0:
        return (True)
    else:
        return (False)


if __name__ == '__main__':
    # Simple tests:
    print(check_brackets('((()))'))  # True
    print(check_brackets('((())())'))  # True
    print(check_brackets('(()()))'))  # False
    print(check_brackets(''))  # False
