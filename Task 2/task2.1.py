# Написать функцию, принимающую на вход строку из последовательности круглых скобок
# и возвращающую True если последовательность верна и False - если нет.

def check_brackets(line: str):
    i = 0
    if len(line) > 1:
        while len(line) > 1 and i+1 < len(line):
            if line[i] == '(' and line[i+1] == ')':
                line = line[:i] + line[i+2:]
                i = 0
            else:
                i += 1

        if len(line) > 0:
            return False
        else:
            return True

    else:
        return False


if __name__ == '__main__':
    # Simple tests:
    print(check_brackets('(((((())))))'))  # True

    print(check_brackets('((())())'))  # True
    print(check_brackets('(()()))'))  # False
    print(check_brackets(''))  # False
