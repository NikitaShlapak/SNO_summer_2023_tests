# Написать функцию, которая на вход принимает строку в формате FEN - шахматную позицию.
# На доске находятся ладьи. Функция должна возвращать False, если хотя бы одна ладья атакует другую и True - если нет.

def check_rooks(line: str):
    line = line.split('/')

    board = []

    for i in range(8):
        st = line[i]
        b = []
        for k in range(len(st)):
            if st[k] == 'R':
                b.append(1)
            else:
                for e in range(int(st[k])):
                    b.append(0)
        board.append(b)

    for i in range(8):
        if sum(board[i]) > 1:
            return False

        k = 0
        for j in range(8):
            k += board[j][i]
        if k > 1:
            return False
    else:
        return True

if __name__ == '__main__':
    # Simple tests:
    print(check_rooks('7R/5R2/6R1/1R6/4R3/2R5/3R4/R7'))  # True
    print(check_rooks('7R/2R5/5RR1/1R6/3R2R1/3R3R/2R5/R7'))  # False
    print(check_rooks('8/8/8/8/8/8/8/8'))  # True
    print(check_rooks('8/8/8/8/8/8/8/R7'))  # True