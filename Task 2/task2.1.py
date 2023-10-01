# Написать функцию, принимающую на вход строку из последовательности круглых скобок
# и возвращающую True если последовательность верна и False - если нет.

def check_brackets(line: str):
    for i in range(line.length):
        


if __name__ == '__main__':
    # Simple tests:
    print(check_brackets('((()))'))  # True
    print(check_brackets('((())())'))  # True
    print(check_brackets('(()()))'))  # False
    print(check_brackets(''))  # False
