def init_board(board):
    # return the 3/3 game board
    my_l = board
    for elements in my_l:
        print(*elements)
    return my_l


def get_move(board):
    # asks for player input, return the coordinates of a valid move
    player_input = input('Give the coordinate: ')
    '''if player_input[0] == 'a':
        while board[0][int(player_input[1])-1] != 0:
            print_board('Already taken, give a new one.')
            break
    if player_input[0] == 'b':
        while board[1][int(player_input[1])-1] != 0:
            print_board('Already taken, give a new one.')
            break
    if player_input[0] == 'c':
        while board[2][int(player_input[1])-1] != 0:
            print_board('Already taken, give a new one.')
            break'''
    while 'a' in player_input[0] and player_input[1] in board[0][int(player_input[1])-1] != 0:
        print('Already taken.')
        break

    return player_input


def mark(coordinates, board, player):
    # writes the value of player 1-2 into the row&col element of board
    player_input = coordinates
    for i in player_input:
        if player_input[0] == 'a':
            board[0][int(player_input[1]) - 1] = player
        if player_input[0] == 'b':
            board[1][int(player_input[1]) - 1] = player
        if player_input[0] == 'c':
            board[2][int(player_input[1]) - 1] = player
    return board


def has_won():
    # returs True if player 1 or 2 has three in a row on board
    pass


def is_full(board):
    # retursn true if board is full
    if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        print("The board is full, it's a tie!")
        return True


def print_board(board):
    # prints the board to screen
    print(board)
    print('  1    2   3 ')
    print('A  {} | {} | {} '.format(board[0][0], board[0][1], board[0][2]))
    print('   ---+---+--- ')
    print('B  {} | {} | {} '.format(board[1][0], board[1][1], board[1][2]))
    print('   ---+---+--- ')
    print('C  {} | {} | {} '.format(board[2][0], board[2][1], board[2][2]))


def print_result():
    # print the result of the game
    pass


def tictactoe_game():
    pass


def player_turn():
    pass


def main():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player = 'X'
    init_board(board)

    while is_full(board) != True:
        print_board(board)
        coordinates = get_move(board)
        mark(coordinates, board, player)




if __name__ == '__main__':
    main()
