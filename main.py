# Config
cross = 'X'
circle = 'O'
turn = cross
end = False
global move
theBoard = {'TL': ' ', 'TM': ' ', 'TR': ' ',
            'ML': ' ', 'MM': ' ', 'MR': ' ',
            'LL': ' ', 'LM': ' ', 'LR': ' ', }
moves = ["TL", "TM", "TR", "ML", "MM", "MR", "LL", "LM", "LR"]


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['LL'] + '|' + board['LM'] + '|' + board['LR'])
    print('Turn for ' + turn + '. Move on which space?')


def check_win(board, _turn):
    global end
    x_counter = 0
    zero_counter = 0
    col_number = 0
    for position in board:
        col_number += 1
        if board['TL'] == _turn and board['MM'] == _turn and board['LR'] == _turn:
            print(_turn + "wins")
            end = True
            break
        if board['TR'] == _turn and board['MM'] == _turn and board['LL'] == _turn:
            print(_turn + "wins")
            end = True
            break
        if board[position] == cross:
            x_counter += 1
        if board[position] == circle:
            zero_counter += 1
        if col_number == 3:
            col_number = 0
            if x_counter == 3:
                print(cross + " wins")
                end = True
            elif zero_counter == 3:
                print(circle + " wins")
                end = True
            else:
                x_counter = 0
                zero_counter = 0


def input_move():
    global move
    move = input("TL, TM, TR..\n")
    if move not in moves:
        print("Something went wrong, try again")
        input_move()
    return move


def conflicts_check(moved):
    if cross in theBoard[moved] or circle in theBoard[moved]:
        print("You cant do this.. ")
        global move
        move = input_move()
        conflicts_check(move)


def tie():
    print("No winners.")


def start_game():
    global turn
    global theBoard
    global move
    for i in range(9):
        print_board(theBoard)
        move = input_move()
        conflicts_check(move)
        theBoard[move] = turn
        check_win(theBoard, turn)
        if i == 8:
            tie()
        if end:
            break
        if turn == cross:
            turn = circle
        else:
            turn = cross


# Start
start_game()
