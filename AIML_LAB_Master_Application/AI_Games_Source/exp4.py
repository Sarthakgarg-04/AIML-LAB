import tkinter as tk
from tkinter import messagebox
from functools import partial
from queue import PriorityQueue
from random import sample

# Define the puzzle state representation
class PuzzleState:
    def __init__(self, board):
        self.board = board
        self.size = len(board)
        self.moves = []

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(map(tuple, self.board)))

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])

    def find_blank(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j

    def move(self, direction):
        i, j = self.find_blank()
        if direction == 'up' and i > 0:
            self.board[i][j], self.board[i-1][j] = self.board[i-1][j], self.board[i][j]
            self.moves.append('Up')
        elif direction == 'down' and i < self.size - 1:
            self.board[i][j], self.board[i+1][j] = self.board[i+1][j], self.board[i][j]
            self.moves.append('Down')
        elif direction == 'left' and j > 0:
            self.board[i][j], self.board[i][j-1] = self.board[i][j-1], self.board[i][j]
            self.moves.append('Left')
        elif direction == 'right' and j < self.size - 1:
            self.board[i][j], self.board[i][j+1] = self.board[i][j+1], self.board[i][j]
            self.moves.append('Right')

# Define the GUI class
class PuzzleGUI:
    def __init__(self, master):
        self.master = master
        self.initial_state = None
        self.goal_state = PuzzleState([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        self.current_state = None
        self.moves = 0
        self.create_widgets()

    def create_widgets(self):
        # Initial state grid
        self.initial_frame = tk.Frame(self.master)
        self.initial_frame.grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.initial_frame, text="Initial State").grid(row=0, column=1)
        self.initial_entries = [[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                entry = tk.Entry(self.initial_frame, width=3)
                entry.grid(row=i+1, column=j)
                self.initial_entries[i][j] = entry

        # Add some padding between the grids
        padding_frame = tk.Frame(self.master)
        padding_frame.grid(row=0, column=1, padx=10, pady=10)

        # Goal state grid
        self.goal_frame = tk.Frame(self.master)
        self.goal_frame.grid(row=0, column=2, padx=10, pady=10)
        tk.Label(self.goal_frame, text="Goal State").grid(row=0, column=1)
        self.goal_labels = [[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                label = tk.Label(self.goal_frame, text=i*3 + j + 1)
                label.grid(row=i+1, column=j)
                self.goal_labels[i][j] = label

        self.set_button = tk.Button(self.master, text="Set Initial State", command=self.set_initial_state)
        self.set_button.grid(row=1, columnspan=3)

        # Buttons for moving the blank tile
        self.move_up_button = tk.Button(self.master, text="Up", command=partial(self.move_blank, 'up'), state=tk.DISABLED)
        self.move_up_button.grid(row=2, column=1)

        self.move_down_button = tk.Button(self.master, text="Down", command=partial(self.move_blank, 'down'), state=tk.DISABLED)
        self.move_down_button.grid(row=3, column=1)

        self.move_left_button = tk.Button(self.master, text="Left", command=partial(self.move_blank, 'left'), state=tk.DISABLED)
        self.move_left_button.grid(row=3, column=0)

        self.move_right_button = tk.Button(self.master, text="Right", command=partial(self.move_blank, 'right'), state=tk.DISABLED)
        self.move_right_button.grid(row=3, column=2)

        self.solve_button = tk.Button(self.master, text="Solve", command=self.solve_puzzle, state=tk.DISABLED)
        self.solve_button.grid(row=4, columnspan=3)

        # Move counter
        self.move_counter_label = tk.Label(self.master, text="Moves: 0")
        self.move_counter_label.grid(row=5, columnspan=3)

    def set_initial_state(self):
        initial_board = []
        numbers = sample(range(9), 9)
        k = 0
        for i in range(3):
            row_values = []
            for j in range(3):
                if numbers[k] == 0:
                    blank = (i, j)
                row_values.append(numbers[k])
                k += 1
            initial_board.append(row_values)

        self.initial_state = PuzzleState(initial_board)
        self.current_state = PuzzleState([row[:] for row in initial_board])
        self.update_gui()

    def move_blank(self, direction):
        self.current_state.move(direction)
        self.moves += 1
        self.update_gui()

    def update_gui(self):
        for i in range(3):
            for j in range(3):
                self.initial_entries[i][j].delete(0, tk.END)
                self.initial_entries[i][j].insert(0, str(self.current_state.board[i][j]))
        if self.current_state == self.goal_state:
            messagebox.showinfo("Congratulations!", f"You solved the puzzle in {self.moves} moves!")
            self.solve_button.config(state=tk.DISABLED)
            self.move_up_button.config(state=tk.DISABLED)
            self.move_down_button.config(state=tk.DISABLED)
            self.move_left_button.config(state=tk.DISABLED)
            self.move_right_button.config(state=tk.DISABLED)
        else:
            self.solve_button.config(state=tk.NORMAL)
            self.move_up_button.config(state=tk.NORMAL if self.current_state.find_blank()[0] > 0 else tk.DISABLED)
            self.move_down_button.config(state=tk.NORMAL if self.current_state.find_blank()[0] < 2 else tk.DISABLED)
            self.move_left_button.config(state=tk.NORMAL if self.current_state.find_blank()[1] > 0 else tk.DISABLED)
            self.move_right_button.config(state=tk.NORMAL if self.current_state.find_blank()[1] < 2 else tk.DISABLED)
        self.move_counter_label.config(text=f"Moves: {self.moves}")

    def solve_puzzle(self):
        # Placeholder for solving puzzle
        pass

# Main function
def main():
    root = tk.Tk()
    root.title("8-Puzzle")
    app = PuzzleGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
