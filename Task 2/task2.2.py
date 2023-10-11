# Написать функцию, принимающую на вход строку из последовательности круглых скобок
# и возвращающую True если последовательность верна и False - если нет.
# Реализовать это так, чтобы сложность была не больше О(n).

def check_brackets(line: str):
    i = 0
    l = len(line)

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
    print(check_brackets('((()))'))  # True
    print(check_brackets('((())())'))  # True
    print(check_brackets('(()()))'))  # False
    print(check_brackets(''))  # False
