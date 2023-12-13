import random

# Создание игрового поля
def create_board():
    board = []
    for _ in range(8):
        row = []
        for _ in range(8):
            row.append(random.randint(1, 5))  # Предполагается, что у вас 5 разных цветов
        board.append(row)
    return board

# Вывод игрового поля на экран
def print_board(board):
    for row in board:
        for element in row:
            print(element, end=" ")
        print()

# Проверка наличия трех одинаковых элементов в ряду или столбце
def check_match(board):
    for row in range(8):
        for col in range(6):
            if board[row][col] == board[row][col+1] == board[row][col+2]:
                return True
    for col in range(8):
        for row in range(6):
            if board[row][col] == board[row+1][col] == board[row+2][col]:
                return True
    return False

# Удаление совпадающих элементов
def remove_match(board):
    for row in range(8):
        for col in range(6):
            if board[row][col] == board[row][col+1] == board[row][col+2]:
                board[row][col] = 0
                board[row][col+1] = 0
                board[row][col+2] = 0
    for col in range(8):
        for row in range(6):
            if board[row][col] == board[row+1][col] == board[row+2][col]:
                board[row][col] = 0
                board[row+1][col] = 0
                board[row+2][col] = 0

# Заполнение новыми элементами
def fill_board(board):
    for col in range(8):
        empty_cells = []
        for row in range(8):
            if board[row][col] == 0:
                empty_cells.append(row)
        for row in empty_cells:
            board[row][col] = random.randint(1, 5)

# Основная игровая функция
def play_game():
    board = create_board()

    while True:
        print_board(board)

        if check_match(board):
            remove_match(board)

        row1 = int(input("Введите номер строки первого элемента для обмена: "))
        col1 = int(input("Введите номер столбца первого элемента для обмена: "))
        row2 = int(input("Введите номер строки второго элемента для обмена: "))
        col2 = int(input("Введите номер столбца второго элемента для обмена: "))

        # Проверка, что элементы можно поменять местами
        if abs(row1 - row2) == 1 and col1 == col2 or abs(col1 - col2) == 1 and row1 == row2:
            board[row1][col1], board[row2][col2] = board[row2][col2], board[row1][col1]
            remove_match(board)
            fill_board(board)
            print("--------------------")
        else:
            print("Некорректный ход!")

play_game()

