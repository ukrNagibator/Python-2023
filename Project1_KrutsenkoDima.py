"""Этот код определяет шесть функций: `display_board`, `enter_move`, `make_list_of_free_fields`, `victory_for`, `draw_move` и `krestiki_noliki`
"""
# Import random module
import random

##Функция `display_board` принимает в качестве параметра текущее состояние доски и выводит его на консоль.
def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[0][0], board[0][1], board[0][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[1][0], board[1][1], board[1][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[2][0], board[2][1], board[2][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")

##Функция `enter_move` запрашивает у пользователя его ход, проверяет его правильность и соответствующим образом обновляет доску.
def enter_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move)
        if move >= 1 and move <= 9:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] == " ":
                    board[row][col] = "O"
                    break
                else:
                    print("That square is already occupied.")
        else:
            print("Invalid move. Please enter a number between 1 and 9.")
"""             Мы делим на 3, чтобы определить, в какой строке и столбце находится клетка на доске, соответствующая введенному игроком числу.
                Так как доска имеет размерность 3x3, то каждая строка и столбец содержит по 3 клетки. 
                При этом вводимое число от 1 до 9 соответствует порядковому номеру клетки на доске, начиная с левого верхнего угла и заканчивая правым нижним углом. 
                Поэтому мы вычитаем 1 из введенного числа, чтобы получить номер клетки от 0 до 8, и затем делим на 3, чтобы определить номер строки, и находим остаток от деления на 3, чтобы определить номер столбца."""

'Функция make_list_of_free_fields() принимает текущее состояние доски в виде двумерного списка board. Она проходит по каждой клетке доски и если клетка свободна (т.е. содержит пробел), '
'то добавляет кортеж с координатами этой клетки в список free_fields. В итоге функция возвращает список всех свободных клеток доски в виде списка кортежей. ' \
'Например, если на доске есть свободные клетки в первой строке и втором столбце, то функция вернет список [(0, 0), (0, 1), (0, 2), (1, 1)].'
def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    """Функция `victory_for(board, sign)` проверяет, есть ли на доске выигрышная комбинация для символа `sign` (в данном случае `O` или `X`). """


    for row in range(3):
          """Внутри цикла функция проверяет, совпадают ли символы в 0-й, 1-й и 2-й клетках строки с символом `sign` с 
        помощью условия `if board[row][0] == board[row][1] == board[row][2] == sign:`. Если да, то функция возвращает `True`, что означает, что игрок выиграл."""
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True

    """Затем функция проходит по каждому столбцу доски с помощью цикла `for col in range(3):`. 
        Внутри цикла функция проверяет, совпадают ли символы в 0-й, 1-й и 2-й клетках столбца с символом `sign` с помощью условия
         `if board[0][col] == board[1][col] == board[2][col] == sign:`. Если да, то функция возвращает `True`, что означает, что игрок выиграл."""
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True

    if board[0][0] == board[1][1] == board[2][2] == sign: ##Затем функция проверяет диагонали доски. Сначала она проверяет главную диагональ (от верхнего левого угла до нижнего правого) с помощью условия
        return True                                       ##`if board[0][0] == board[1][1] == board[2][2] == sign:`. Если да, то функция возвращает `True`, что означает, что игрок выиграл.
                                                          ## Затем функция проверяет побочную диагональ (от верхнего правого угла до нижнего левого) с помощью условия `if board[0][2] == board[1][1] == board[2][0] == sign:`.
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

##Функция `draw_move` выбирает случайную свободную клетку и помещает туда  'X'.
def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if not free_fields:
        return False
    row, col = random.choice(free_fields)
    board[row][col] = "X"
    return True

##Функция `krestiki_noliki` создаёт доску, отображает ее и запускает цикл, в котором игрок и компьютер по очереди делают ходы, пока игра не закончится.
def krestiki_noliki():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    board[1][1] = "X"
    display_board(board)
    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, "O"):
            print("You win!")
            break
        if not draw_move(board):
            print("It's a draw!")
            break
        display_board(board)
        if victory_for(board, "X"):
            print("Computer wins!")
            break
krestiki_noliki()
