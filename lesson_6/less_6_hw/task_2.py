import random

from packet import chess


def random_coords():
    x_coords = [i for i in range(1, 9)]
    y_coords = [i for i in range(1, 9)]
    random.shuffle(x_coords)
    random.shuffle(y_coords)
    return list(zip(x_coords, y_coords))


count = 0
temp = 0
while count < 4:
    temp += 1
    queens_coords = random_coords()
    if chess.check_eight_queens(queens_coords):
        print(f'Попытка № {temp}')
        print(queens_coords)
        chess.draw_board(queens_coords)
        count += 1