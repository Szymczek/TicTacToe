# Config
end = False
theBoard = {'TL': ' ', 'TM': ' ', 'TR': ' ',
            'ML': ' ', 'MM': ' ', 'MR': ' ',
            'LL': ' ', 'LM': ' ', 'LR': ' ', }
moves = ["TL", "TM", "TR", "ML", "MM", "MR", "LL", "LM", "LR"]


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.sign = ''
        self.move = ''

    def get_point(self):
        self.score += 1

    def set_sign(self, sign):
        self.sign = sign

    def input_move(self, ):
        self.move = input("TL, TM, TR..\n")
        if self.move not in moves:
            print("Something went wrong, try again")
            self.input_move()


def print_board(board, player):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['LL'] + '|' + board['LM'] + '|' + board['LR'])
    print('Turn for ' + player + '. Move on which space?')


def clear_board():
    global theBoard
    theBoard = {'TL': ' ', 'TM': ' ', 'TR': ' ',
                'ML': ' ', 'MM': ' ', 'MR': ' ',
                'LL': ' ', 'LM': ' ', 'LR': ' ', }


def small_brain_checks_win(board, player):
    """ Checks possible wins, easy way"""
    global end
    # Diagonal
    if board['TL'] == player.sign and board['MM'] == player.sign and board['LR'] == player.sign:
        print(player.name + " wins")
        player.get_point()
        end = True
    if board['TR'] == player.sign and board['MM'] == player.sign and board['LL'] == player.sign:
        print(player.name + " wins")
        player.get_point()
        end = True
    # Rows
    if board['TL'] == player.sign and board['TM'] == player.sign and board['TR'] == player.sign:
        print(player.name + " wins")
        player.get_point()
        end = True
    if board['ML'] == player.sign and board['MM'] == player.sign and board['MR'] == player.sign:
        print(player.name + " wins")
        player.get_point()
        end = True
    if board['LL'] == player.sign and board['LM'] == player.sign and board['LR'] == player.sign:
        print(player.name + " wins")
        player.get_point()
        end = True
    # Columns
    if board['TL'] == player.sign and board['ML'] == player.sign and board['LL'] == player.sign:
        print(player.name + " wins")
        player.get_point()
        end = True
    if board['TM'] == player.sign and board['MM'] == player.sign and board['LM'] == player.sign:
        print(player.name + " wins")
        player.get_point()
        end = True
    if board['TL'] == player.sign and board['MR'] == player.sign and board['LR'] == player.sign:
        print(player.name + " wins")
        player.get_point()
        end = True


def conflicts_check(player, player2, sign1, sign2):
    if player.move not in moves:
        print("")
        player.input_move()
        conflicts_check(player, player2,  player.sign, player2.sign)
    if sign1 in theBoard[player.move] or sign2 in theBoard[player.move]:
        print("You cant do this.. ")
        player.input_move()
        conflicts_check(player, player2,  player.sign, player2.sign)


def tie():
    global end
    print("No winners.")
    end = True


def start_game(player1, player2):
    global theBoard
    global end
    player1.set_sign('X')
    player2.set_sign('O')
    for round in range(9):
        if round == 8:
            tie()
        if end:
            print("Score for " + player1.name + ": " + str(player1.score) + ".")
            print("Score for " + player2.name + ": " + str(player2.score) + ".")
            restart = input("Wanna play more? Y/N\n")
            if restart == 'Y':
                clear_board()
                start_game(player1, player2)
            else:
                end = False
                break
        if round % 2 == 0:
            print_board(theBoard, player1.name)
            player1.input_move()
            conflicts_check(player1, player2, player1.sign, player2.sign)
            theBoard[player1.move] = player1.sign
            small_brain_checks_win(theBoard, player1)
        else:
            print_board(theBoard, player2.name)
            player2.input_move()
            conflicts_check(player2, player1, player1.sign, player2.sign)
            theBoard[player2.move] = player2.sign
            small_brain_checks_win(theBoard, player2)



# Start
p1 = Player("Szymi")
p2 = Player("Random")
start_game(p1, p2)
