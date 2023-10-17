# Написать функцию, принимающую на вход строку из последовательности круглых скобок
# и возвращающую True если последовательность верна и False - если нет.
# Реализовать это так, чтобы сложность была не больше О(n).

def check_brackets(line: str):
    line_list = list(line)
    stack = []
    if not line_list:
        return False
    for el in line_list:
        if el == '(':
            stack.append(el)
        else:
            if not len(stack):
                return False
            else:
                stack.pop(-1)
    return not stack


if __name__ == '__main__':
    # Simple tests:
    print(check_brackets('((()))'))  # True
    print(check_brackets('((())())'))  # True
    print(check_brackets('(()()))'))  # False
    print(check_brackets(''))  # False
