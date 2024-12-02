#!/usr/bin/env python3
"""
AOC Day 4 - Bingo Board
"""

__author__ = "Ritesh Kumar"

# a bingo board is predefined to be a 5x5 grid
class BingoBoard:
    def __init__(self, board_lines):
        self.board_lines = board_lines
        self.current_unmarked_sum = sum(sum(board_lines, [])) # pythonic way of summing 2d arr
        self.has_won = False
        self.current_pick = -1 # starting value, assuming that bingo board will never have negative nums
        return

    # checks row-wise then column wise to see if there's a win
    def check_for_wins(self):
        # check rows and cols in single pass:
        for idx in range(len(self.board_lines)):
            row = self.board_lines[idx]
            col = [r[idx] for r in self.board_lines] # hooray for list comprehension in python
            is_winning_row = len(set(row)) == 1 and self.board_lines[idx][0] == -1
            is_winning_col = len(set(col)) == 1 and self.board_lines[0][idx] == -1
            if(is_winning_col or is_winning_row):
                self.has_won = True
                return True

    # combs thru in O(n^2)
    def play_round(self, pick):
        self.current_pick = pick
        for row in range(len(self.board_lines)):
            for col in range(len(self.board_lines[row])):
                val = self.board_lines[row][col]
                if (val == pick):
                    self.current_unmarked_sum -= val
                    self.board_lines[row][col] = -1 # marks visited
        self.check_for_wins()

    def get_score(self):
        return self.current_unmarked_sum * self.current_pick

def init_game():
    bingo_boards = []
    with open("input") as f:
        inputs = list(map(lambda x:(x.rstrip("\n")), f.readlines()))
    picks = inputs[0].split(",")
    board_buffer = []
    for line in inputs[1:]:
        if not line:
            if board_buffer:
                bingo_boards.append(BingoBoard(board_buffer))
                board_buffer = [] # flush when done
        else:
            board_buffer.append(list(map(lambda x:int(x),line.split())))
    if board_buffer: # last board in buffer
        bingo_boards.append(BingoBoard(board_buffer))
    return [picks, bingo_boards]

def main():
    picks, bingo_boards = init_game()
    winners = []
    for pick in picks:
        for board in bingo_boards:
            if not board.has_won:
                board.play_round(int(pick))
                if board.has_won:
                    winners.append(board)
    print(f"The first winning board will have a score of {winners[0].get_score()} and the last winning board will have a score of {winners[-1].get_score()}")
    return


if __name__ == "__main__":
    main()
