# from random import randint

class Board:

    def __init__(self):
        # tworzenie pustej tablicy
        self.board = [' ' for _ in range(10)]

    def __str__(self):
        return (
                f'{self.board[7]}' + ' | ' + f'{self.board[8]}' + ' | ' + f'{self.board[9]}\n' +
                f'_'*9 + '\n'
                f'{self.board[4]}' + ' | ' + f'{self.board[5]}' + ' | ' + f'{self.board[6]}\n' +
                f'_'*9 + '\n'        
                f'{self.board[1]}' + ' | ' + f'{self.board[2]}' + ' | ' + f'{self.board[3]}\n'
                )

    def add_to_board(self, place: int, marker: str, player_set: set):
        if place in player_set:
            raise ValueError('Error in Board class add_to_board. Wrong number')
        elif place not in player_set:
            self.board.pop(place)
            self.board.insert(place, marker)


class Player:
    def __init__(self, marker):
        self.marker = marker
        self.player_set = set()

    def __str__(self):
        return f'Player {self.marker}'

    def place(self):
        place_to_choose = int(input('Select number 1-9 to place marker there: '))
        if place_to_choose in range(1, 10):
            return place_to_choose
        else:
            raise ValueError


def win_check(player_set, player):
    win_set = [{1,2,3}, {4,5,6}, {7,8,9}, {1,4,7}, {2,5,8}, {3,6,9}, {1,5,9}, {3,5,7}]
    for w_set in win_set:
        if player_set.intersection(w_set) in win_set:
            print(f'Player {player.marker} wins the game !')
            return 'Finished Game'


def round_flow(player, board, used_position_set):
    try:
        print(f'{player} turn')
        player_place = player.place()
        if player_place in used_position_set:
            raise ValueError
        else:
            board.add_to_board(player_place, player.marker, used_position_set)
            used_position_set.add(player_place)
            player.player_set.add(player_place)
            return 'Done'
    except ValueError:
        print('Choose correct number')
    finally:
        print(board)


def player_one_marker():
    marker = input('Choose X or O: ').upper()
    while marker not in ["X", "O"]:
        marker = input('Choose X or O: ').upper()

    return marker


board = Board()
#      WYBÓR GRACZY

print('Tic Tac Toe')
marker = player_one_marker()
used_position_set = set()
player_one = Player(marker)


if player_one.marker == 'X':
    player_two = Player('O')

else:
    player_two = Player('X')

#      GAMEFLOW

print(board)
while len(used_position_set) != 9:
    player_one_turn = True
    while player_one_turn:
        if round_flow(player_one, board, used_position_set) == 'Done':
            player_one_turn = False
        elif ValueError:
            continue
        else:
            player_one_turn = False

    if win_check(player_one.player_set, player_one) == 'Finished Game':
        break

    player_two_turn = True
    while player_two_turn:
        if round_flow(player_two, board, used_position_set) == 'Done':
            player_two_turn = False
        elif ValueError:
            continue
        else:
            player_two_turn = False
    if win_check(player_two.player_set, player_two) == 'Finished Game':
        break

#### warunek braku wygranej