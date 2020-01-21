from os import system as system
import random


def menu(menu_list):
    for i, m_list in enumerate(menu_list, 1):
        print(f'({i}) {menu_list[i - 1]}')


def init_board():
    # return the 3/3 game board
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    return board


def main_input():
    user_input = input("\nWhich options you would like to choose?: \n")
    return user_input


def get_move(board, player):
    # asks for player input, return the coordinates of a valid move
    clearing = '\033c'
    check_words = ['a', 'b', 'c']
    check_numbers = ['1', '2', '3']
    board_index = ''
    player_turn = player

    while True:

        if player_turn == 'O':
            player_turn = 'player one'
        elif player_turn == 'X':
            player_turn = 'player two'
        player_input = input(f'Give the {player_turn} coordinate: ').lower()
        if player_input == 'quit':
            quit()
        if len(player_input) != 2:
            print(clearing)
            print_board(board)
            print('Give only two character.')
            player_input = input(f'Give the {player_turn} coordinate: ').lower()
            continue
        if player_input[0] not in check_words or player_input[1] not in check_numbers:
            print(clearing)
            print_board(board)
            print("Give a valid coordinate.")
            player_input = input(f'Give the {player_turn} coordinate: ').lower()
            print(clearing)
            continue
        else:
            if player_input[0] == 'a':
                board_index = 0
                print(clearing)
            elif player_input[0] == 'b':
                board_index = 1
                print(clearing)
            elif player_input[0] == 'c':
                board_index = 2
                print(clearing)
            while board[board_index][int(player_input[1]) - 1] != ' ':
                print(clearing)
                print_board(board)
                print('Already taken, give a new one.')
                player_input = input(f'Give the {player_turn} coordinate: ').lower()
            return player_input


def get_ai_move(board, player):
    while True:
        ai_row = random.randrange(0, 2)
        ai_column = random.randrange(0, 2)
        if board[ai_row][ai_column] != ' ':
            continue
        else:
            board[ai_row][ai_column] = player
            return board


def mark(coordinates, board, player):
    # writes the value of player 1-2 into the row&col element of board
    player_input = coordinates
    for i in player_input:
        if player_input[0] == 'a':
            board[0][int(player_input[1]) - 1] = player
        elif player_input[0] == 'b':
            board[1][int(player_input[1]) - 1] = player
        elif player_input[0] == 'c':
            board[2][int(player_input[1]) - 1] = player
    return board


def has_won(board, player):
    # returs True if player 1 or 2 has three in a row on board
    board_colum_a = [board[0][0], board[1][0], board[2][0]]  # [1,4,7]
    board_colum_b = [board[0][1], board[1][1], board[2][1]]  # [2,5,8]
    board_colum_c = [board[0][2], board[1][2], board[2][2]]  # [3,6,9]
    column = [board_colum_a, board_colum_b, board_colum_c]  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    board_diag_a = [board[0][0], board[1][1], board[2][2]]
    board_diag_b = [board[0][2], board[1][1], board[2][1]]
    diagonal = [board_diag_a, board_diag_b]

    for columns in column:
        if columns[0] == player and columns[1] == player and columns[2] == player:
            print(player + " won")
            return True
    for rows in board:
        if player == rows[0] and player == rows[1] and player == rows[2]:
            print(player, " has won")
            return True
    for diagonal_row in diagonal:
        if player == diagonal_row[0] and player == diagonal_row[1] and player == diagonal_row[2]:
            print(player, " has won")
            return True


def is_full(board):
    # return true if board is full
    if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
        print("The board is full, it's a tie!")
        return True


def print_board(board):
    # prints the board to screen
    print('  1    2   3 ')
    print('A  {} | {} | {} '.format(board[0][0], board[0][1], board[0][2]))
    print('  ---+---+--- ')
    print('B  {} | {} | {} '.format(board[1][0], board[1][1], board[1][2]))
    print('  ---+---+--- ')
    print('C  {} | {} | {} '.format(board[2][0], board[2][1], board[2][2]))


def tictactoe_game(turn, board):
    system('clear')
    print('         TIC-TAC-TOE by SAD\n')
    menu_list = ['Player vs Player', 'Player vs AI', 'Credit', 'Quit']
    player = ''
    while True:
        menu(menu_list)
        user_menu_input = main_input()
        system('clear')
        if user_menu_input == '1':
            print_board(board)
            while not is_full(board) and not has_won(board, player):

                coordinates = get_move(board, player)
                if turn % 2 == 1:
                    player = 'X'
                else:
                    player = 'O'
                mark(coordinates, board, player)
                print_board(board)
                turn += 1

        elif user_menu_input == '2':
            ai_turn = turn
            print_board(board)
            while not is_full(board) and not has_won(board, player):

                coordinates = get_move(board, player)
                if ai_turn % 2 == 1:
                    player = 'X'
                else:
                    player = 'O'
                mark(coordinates, board, player)
                print_board(board)
                ai_turn += 1
                system('clear')
                if ai_turn % 2 == 1:
                    player = 'X'
                else:
                    player = 'O'
                get_ai_move(board, player)
                print_board(board)
                ai_turn += 1

        elif user_menu_input == '3':
            print("Made by SAD\nSzili\nDani")

        elif user_menu_input == '4':
            print(" Thanks for playing, C YA")
            quit()


def main():
    board = init_board()
    print('\033c')
    print_board(board)
    player_turn = 1
    tictactoe_game(player_turn, board)


if __name__ == '__main__':
    main()
