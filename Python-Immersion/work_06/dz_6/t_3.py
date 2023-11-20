import random

def generate_board():
    # Генерируем случайную доску
    board = []

    for i in range(1, 8+1):
        queen = (i, random.randint(1, 8))
        board.append(queen)
    return board

def is_attacking(q1, q2):
    x1, y1 = map(int, q1)
    x2, y2 = map(int, q2)
    step_x = abs(x2 - x1)
    step_y = abs(y2 - y1)
    if step_x == step_y:            # Так ходит слон
        # print('бьёт')
        return True
    elif x1 == x2 or y1 == y2:      # Так ходит ладья
        # print('бьёт')
        return True
    else:
        # print('не бьёт')
        return False

def check_queens(comb):
    for i in range(len(comb)):
        for j in range(i+1, len(comb)):
            if is_attacking(comb[i], comb[j]):
                return False
    return True

def generate_boards():
    # Генерируем доски, пока не получим 4 успешные расстановки
    count = 0
    board_list = []
    while count < 4:
        board = generate_board()
        if check_queens(board):
            count += 1
            board_list.append(board)
    return board_list

print(generate_boards())