import random


def to_int_or_default(val, default):
    try:
        return int(val)
    except ValueError:
        return default


class Minesweeper:
    BOMB = '*'
    EMPTY = '_'
    FLAGGED = '^'
    UNREVEALED = '?'

    def __init__(self, rows=9, cols=9, bombs=10, revealed=False):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.table = [[self.EMPTY] * cols for _ in range(rows)]
        self.revealed = [[revealed] * cols for _ in range(rows)]
        self.flagged = [[False] * cols for _ in range(rows)]
        self.game_over = False
        self.add_bombs()
    
    def add_bombs(self, ):
        for _ in range(self.bombs):
            row, col = random.randrange(self.rows), random.randrange(self.cols)
            while self.is_bomb(row, col):
                row, col = random.randrange(self.rows), random.randrange(self.cols)
            self.table[row][col] = self.BOMB
            self.set_bomb_counter(row, col)
    
    @property
    def has_won(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.revealed[i][j] and self.table[i][j] != self.BOMB:
                    return False
        return True
    
    def is_bomb(self, row, col):
        return self.table[row][col] == self.BOMB
    
    def increase_bomb_counter(self, row, col):
        if self.table[row][col] != self.BOMB:
            self.table[row][col] = to_int_or_default(self.table[row][col], default=0) + 1
    
    def set_bomb_counter(self, row, col):
        for r, c in self.get_valid_surrounding_squares(row, col):
            self.increase_bomb_counter(r, c)
    
    def get_valid_surrounding_squares(self, row, col):
        surrounding = [
            (row-1, col-1), (row-1, col), (row-1, col+1),
            (row, col-1), (row, col+1),
            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
        ]
        return [(r, c) for (r, c) in surrounding if 0 <= r < self.rows and 0 <= c < self.cols]
    
    def printed_value(self, row, col):
        if self.revealed[row][col]:
            return str(self.table[row][col])
        elif self.flagged[row][col]:
            return self.FLAGGED
        return self.UNREVEALED
    
    def print_board(self):
        for row in range(self.rows):
            print(' '.join(
                [self.printed_value(row, col) for col in range(self.cols)]
            ))
    
    def reveal_square(self, row, col):
        if self.revealed[row][col]:
            print('You have already revealed this square.')
        elif self.flagged[row][col]:
            print('You need to unflag this square before revealing it.')
        elif self.table[row][col] == self.BOMB:
            self.game_over = True
        elif self.table[row][col] == self.EMPTY:
            self.reveal_all_surrounding_numbers(row, col)
        else:
            self.revealed[row][col] = True
    
    def reveal_all_surrounding_numbers(self, row, col):
        if self.revealed[row][col]:
            return
        self.revealed[row][col] = True
        if self.table[row][col] == self.EMPTY:
            for r, c in self.get_valid_surrounding_squares(row, col):
                self.reveal_all_surrounding_numbers(r, c)

    def reveal_all(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.revealed[i][j] = True
    
    def flag(self, row, col):
        if not self.flagged[row][col] and not self.revealed[row][col]:
            self.flagged[row][col] = True
        else:
            print('Cannot flag this square.')
    
    def unflag(self, row, col):
        if self.flagged[row][col] and not self.revealed[row][col]:
            self.flagged[row][col] = False
        else:
            print('Cannot unflag this square because it is not flagged.')


class Game:
    def __init__(self, rows=9, cols=9, bombs=10):
        self.board = Minesweeper(rows=rows, cols=cols, bombs=bombs)
    
    def play(self):
        self.board.print_board()
        print('')
        while not self.board.game_over and not self.board.has_won:
            if self.run_next_command():
                self.board.print_board()
                print('')
        self.board.reveal_all()

        print('======================================')

        self.board.print_board()
        print('')
        if self.board.game_over:
            print('Sorry, better luck next time!')
        else:
            print('Hurray! You won!!!')
    
    def read_command(self, prompt):
        return tuple(filter(lambda s: len(s), input(prompt).strip().lower().split(' ')))
    
    def cmd_error(self):
        print('Command needs to be of the format <CMD> <row> <col>, ex. reveal 2 5')
    
    def run_next_command(self):
        try:
            cmd, row, col = self.read_command('Enter command: ')
            row, col = int(row), int(col)
            if cmd not in ['reveal', 'flag', 'unflag']:
                self.cmd_error()
                return False
            elif cmd == 'reveal':
                self.board.reveal_square(row, col)
            elif cmd == 'flag':
                self.board.flag(row, col)
            elif cmd == 'unflag':
                self.board.unflag(row, col)
            return True
        except ValueError:
            self.cmd_error()
            return False


Game().play()
