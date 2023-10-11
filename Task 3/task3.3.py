# Написать функцию, которая на вход принимает строку в формате FEN - шахматную позицию.
# На доске находятся ферзи. Функция должна возвращать False, если хотя бы одна ладья атакует другую и True - если нет.
# Вместе с ответом True должен выводиться список всех полей, на которые ещё можно поставить ферзя без нарушения правила.

import chess
import chess.svg


def check_rooks(line: str):
    board = chess.Board(line)



if __name__ == '__main__':
    # Simple tests:
    print(check_rooks('8/8/8/7Q/4Q3/1Q6/3Q4/Q7'))  # True, [с7,c8,f8]
    print(check_rooks('8/3Q4/6Q1/4Q3/2Q4Q/Q4Q2/8/1Q6'))  # False

    with open("board.svg", 'w') as svg:
        board = chess.Board("8/8/8/7Q/4Q3/1Q6/3Q4/Q7 w - - 0 1")
        svg.write(
            chess.svg.board(board=board, fill=dict.fromkeys([50, 58, 61], "#cc0000cc"), size=350)
        )
