import sys

class ConnectFour:
    def __init__(self, rows: int = 6, cols: int = 7):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.current_player = 'X'

    def print_board(self):
        for idx, row in enumerate(self.board):
            if idx == 0:
                print(" ".join([str(x)for x in range(1, self.cols + 1)]))
            print('|'.join(row))
            print('-' * (self.cols * 2 - 1))

    def apply_move(self, column_name: int):
        while column_name not in range(1, self.cols + 1):
            print(f"Invalid move, choose value from 1 to {self.cols}")
            column_name = self.choose_move(message = f"Player {self.current_player} your turn")

        for row_idx in range(self.rows - 1, -1, -1):
            if self.board[row_idx][column_name-1] == ' ':
                self.board[row_idx][column_name-1] = self.current_player
                break
            elif row_idx == 0:
                move_index = self.choose_move(message=f"Player {self.current_player}, choose another column as it is busy")
                self.apply_move(column_name=move_index)

    def choose_move(self, message = None):
        if message is not None:
            print(message)
        while True:
            try:
                column_num = int(input(f"Player {self.current_player} enter column to move (1-{self.cols}): "))
                if column_num in range(1, self.cols + 1):
                    return column_num
                else:
                    print(f"Invalid move, choose a value from 1 to {self.cols}")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def switch_player(self):
        self.current_player = "0" if self.current_player == 'X' else "X"


    def _sliding_window_summ(self, array: list[str], type_check: str):
        for item in range(self.cols - 3):
            if sum(1 if x == self.current_player else 0 for x in array[item: item + 5]) >= 4:
                print(f"Player {self.current_player} won!")
                print(f"4 in a {type_check} crossed!")
                sys.exit(0)

    def check_winner(self):
        # horizontal
        for row in self.board:
            self._sliding_window_summ(array=row, type_check="row")

        # vertical
        for col in range(self.cols):
            # creating row from columns
            column = []
            for row in self.board:
                column.append(row[col])
            self._sliding_window_summ(array=column, type_check="column")

        # diagonal
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row + i][col + i] == self.current_player for i in range(4)):
                    print(f"Player {self.current_player} won!")
                    print(f"4 in a diagonal crossed!")
                    sys.exit(0)
            for col in range(3, self.cols):
                if all(self.board[row + i][col - i] == self.current_player for i in range(4)):
                    print(f"Player {self.current_player} won!")
                    print(f"4 in a diagonal crossed!")
                    sys.exit(0)


    def play(self):
        print("Welcome to Connect Four!")
        self.print_board()
        while True:
            move_index = self.choose_move(message = f"Player {self.current_player} your turn")
            self.apply_move(move_index)
            self.print_board()
            self.check_winner()
            self.switch_player()



if __name__ == "__main__":
    game = ConnectFour()
    game.play()
