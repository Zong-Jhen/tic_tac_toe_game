# 先用random當作例子
import random


class RandomPlayer:
    """
    This player is for ai.

    A tic tac toe game:
    |1|2|3| (0,0)|(0,1)|(0,2)
    |4|5|6| (1,0)|(1,1)|(1,2)
    |7|8|9| (2,0)|(2,1)|(2,2)

    ############################
    Design of board:
    0: empty
    1: O
    2: X

    """

    def __init__(self, turn: int) -> None:
        self.turn = turn

    # 先找到棋盤上空的點
    def get_legal_move(self, board) -> list:
        return_list = []
        for i, row in enumerate(board):  # game.py 裡面的棋盤是二維
            for j, item in enumerate(row):  # 每個row分開檢查
                if item == 0:
                    return_list.append(i * 3 + j + 1)
        return return_list

    def generate_move(self, board) -> int:
        # 不是player決定而是電腦決定
        # num = input("enter a move: ")
        # return int(num)
        legal_move = self.get_legal_move(board)
        return random.choice(legal_move)


if __name__ == "__main__":  # utls.py 也有做過
    p = RandomPlayer(0)
    legal_move = p.get_legal_move([[0, 1, 2], [0, 1, 0], [0, 0, 0]])
    print(legal_move)
    print(p.generate_move([[0, 1, 2], [0, 1, 0], [0, 0, 0]]))
