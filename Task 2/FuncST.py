def check_brackets(line: str):
    c = 0
    if len(line) == 0:
        return (False)
    for i in range(len(line)):
        if line[i] == '(':
            c = c+1
        if line[i] == ')':
            c = c-1
    if c == 0:
        return (True)
    else:
        return (False)


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
