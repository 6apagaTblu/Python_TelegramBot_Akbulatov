from colorama import init, Fore, Back

def draw_board(board):
    """Рисование доски 3х3"""
    print('---------')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                print(Back.BLUE + board[i][j] + Back.RESET, end='')
            elif board[i][j] == 'X':
                print(Back.GREEN + Fore.RED + board[i][j] + Back.RESET + Fore.RESET, end = '')
            else:
                print(Back.YELLOW + Fore.BLACK + board[i][j] + Back.RESET + Fore.RESET, end = '')
            if j < 2:
                print(' | ', end = '')
            else:
                print('')
        print('---------')

def ask_and_make_move(player, board):
    """Запрос и выполнение хода"""
    x, y = ask_move(player, board)
    make_move(player, board, x, y)

def ask_move(player, board):
    """Запрос хода"""
    try:
        x, y = input(f'Ход игрока {player}. Введите координаты (через пробел)').split()
    except ValueError:
        print('Необходимо ввести ровно две координаты')
        return ask_move(player, board)

    try:
        x, y = int(x), int(y)
    except ValueError:
        print('Необходимо ввести координаты в числовом формате')
        return ask_move(player, board)

    if (0 <= x <= 2) and (0 <= y <= 2):
        if board[x][y] == ' ':
            return (x, y)
        else:
            print('Поле занято, введите новые координаты')
            return ask_move(player, board)
    else:
        print('Координаты выходят за границы диапазона')
        return ask_move(player, board)

def make_move(player, board, x, y):
    """Выполнение хода"""
    board[x][y] = player

def check_win(player, board):
    """Проверка выигрыша"""
    # Проверка строк и столбцов
    for i in range(3):
        # Проверка строк
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        # Проверка столбцов
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[2][0] == board[1][1] == board[0][2] == player:
        return True
    return False

def tic_tac_toe():
    """Основной ход игры"""
    while True:
        # Рисуем пустую доску
        board = [[' ' for _ in range(3)] for i in range (3)]
        draw_board(board)

        player = 'X'
        while True:
            ask_and_make_move(player, board)
            draw_board(board)
            # Проверяем на выигрыш
            if check_win(player, board):
                print(f'Выиграл игрок {player}!')
                break
            # Проверяем на заполненность
            isFull = True
            for i in range(3):
                if ' ' in board[i]:
                    isFull = False
                    break
            if isFull:
                print('На доске больше нет свободных полей')
                break

            if player == 'X':
                player = 'Y'
            else:
                player = 'X'

        restart = input('Хотите ли сыграть снова?(y/n)')
        if restart.lower() != 'y':
            break

init()
tic_tac_toe()