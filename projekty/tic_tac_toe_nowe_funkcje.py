class Player:
    def __init__(self, marker: str):
        self.marker = marker
        self.player_set = set()

    def __str__(self):
        return f'Player {self.marker}'

    def place(self):
        place_to_choose = input('Select number 1-9 to place marker there: ')
        if int(place_to_choose) in range(1, 10):
            return int(place_to_choose)


class Board:

    board = [x for x in range(10)]
    win_set = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
    used_position_set = set()

    def __str__(self):
        return (
                f'{self.board[7]}' + ' | ' + f'{self.board[8]}' + ' | ' + f'{self.board[9]}\n' +
                f'_'*9 + '\n'
                         f'{self.board[4]}' + ' | ' + f'{self.board[5]}' + ' | ' + f'{self.board[6]}\n' +
                f'_'*9 + '\n'
                         f'{self.board[1]}' + ' | ' + f'{self.board[2]}' + ' | ' + f'{self.board[3]}\n'
        )

    def add_to_board(self, place: int, marker: str, player_set: set):
        if place not in player_set:
            self.board.pop(place)
            self.board.insert(place, marker)

    def win_check(self, player: Player):
        for w_set in self.win_set:
            if player.player_set.intersection(w_set) in self.win_set:
                print(f'Player {player.marker} wins the game !')
                return True
        else:
            return False


def round_flow(player: Player, board: Board, used_position_set: set):
    try:
        print(f'{player} turn')
        player_place = player.place()
        while player_place not in range(1, 10):
            print('--Wrong number--')
            player_place = player.place()

        if player_place not in used_position_set:
            board.add_to_board(player_place, player.marker, used_position_set)
            used_position_set.add(player_place)
            player.player_set.add(player_place)

            return 'Done'
        else:
            print('-Choose unoccupied place-')
    except ValueError:
        print('! ! The integer seems to be not ! !')
    finally:
        print(board)
        if board.win_check(player):
            exit()
        elif board.win_check(player) is False and len(used_position_set) == 9:
            print("++++ REMIS SREMIS ++++")
            exit()


def player_one_marker():
    marker = input('Choose X or O: ').upper()
    while marker not in ["X", "O"]:
        marker = input('Choose X or O: ').upper()

    return marker


board = Board()
print('Tic Tac Toe')

marker = player_one_marker()
player_one = Player(marker)
#      WYBÓR GRACZY
if player_one.marker == 'X':
    player_two = Player('O')

else:
    player_two = Player('X')

#      GAMEFLOW


print(board)
while len(board.used_position_set) != 9:
    player_one_turn = True
    while player_one_turn:
        if round_flow(player_one, board, board.used_position_set) == 'Done':
            player_one_turn = False
        else:
            player_one_turn = True

    player_two_turn = True
    while player_two_turn:
        if round_flow(player_two, board, board.used_position_set) == 'Done':
            player_two_turn = False
        else:
            player_two_turn = True
