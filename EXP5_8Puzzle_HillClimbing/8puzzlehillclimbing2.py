import tkinter as tk
from tkinter import messagebox

class EightPuzzleGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("8 Puzzle")
        self.master.geometry("300x300")
        
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
        self.empty_pos = (2, 2)  # Coordinates of the empty tile
        self.shuffle_board()

        self.tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                if self.board[i][j] is not None:
                    tile = tk.Button(master, text=str(self.board[i][j]), width=5, height=2,
                                     command=lambda i=i, j=j: self.move_tile(i, j))
                    tile.grid(row=i, column=j)
                    row.append(tile)
                else:
                    row.append(None)
            self.tiles.append(row)

    def shuffle_board(self):
        # Shuffle the board randomly
        import random
        nums = list(range(1, 9))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                if (i, j) != self.empty_pos:
                    self.board[i][j] = nums.pop()

    def move_tile(self, i, j):
        # Move the tile at position (i, j) if possible
        if self.can_move(i, j):
            self.board[self.empty_pos[0]][self.empty_pos[1]] = self.board[i][j]
            self.board[i][j] = None
            self.empty_pos = (i, j)
            self.update_gui()

    def can_move(self, i, j):
        # Check if the tile at position (i, j) can be moved
        if abs(self.empty_pos[0] - i) + abs(self.empty_pos[1] - j) == 1:
            return True
        return False

    def update_gui(self):
        # Update the GUI to reflect the current state of the board
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is not None:
                    self.tiles[i][j].config(text=str(self.board[i][j]))

    def is_goal_state(self):
        # Check if the current state of the board is the goal state
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, None]]


if __name__ == "__main__":
    root = tk.Tk()
    app = EightPuzzleGUI(root)
    root.mainloop()
