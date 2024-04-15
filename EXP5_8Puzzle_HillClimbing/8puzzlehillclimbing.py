import tkinter as tk
from tkinter import messagebox
import random

class EightPuzzleGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("8 Puzzle")
        
        self.initial_state = [1, 2, 3, 4, 5, 6, 7, 0, 8]  
        self.current_state = self.initial_state.copy()
        
        self.shuffle_button = tk.Button(master, text="Shuffle", command=self.shuffle)
        self.shuffle_button.pack()

        self.solve_button = tk.Button(master, text="Solve", command=self.solve)
        self.solve_button.pack()

        self.tiles = []
        for i in range(3):
            for j in range(3):
                tile = tk.Button(master, text=str(self.current_state[i*3 + j]), font=("Arial", 20), width=6, height=3)
                tile.config(command=lambda button=tile: self.move(button))
                tile.grid(row=i+1, column=j, padx=5, pady=5)
                self.tiles.append(tile)
                
    def shuffle(self):
        random.shuffle(self.current_state)
        self.update_tiles()

    def move(self, button):
        current_index = self.tiles.index(button)
        row, col = divmod(current_index, 3)
        empty_tile_index = self.current_state.index(0)
        empty_row, empty_col = divmod(empty_tile_index, 3)
        
        if (abs(row - empty_row) == 1 and col == empty_col) or (abs(col - empty_col) == 1 and row == empty_row):
            self.current_state[empty_tile_index], self.current_state[current_index] = self.current_state[current_index], self.current_state[empty_tile_index]
            self.update_tiles()
            self.check_win()

    def update_tiles(self):
        for i in range(9):
            self.tiles[i].config(text=str(self.current_state[i]))
        
    def check_win(self):
        if self.current_state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            messagebox.showinfo("Congratulations!", "You solved the puzzle!")

    def solve(self):
        solved_state = hill_climbing(self.current_state)
        if solved_state is not None:
            self.current_state = solved_state
            self.update_tiles()
            self.check_win()
        else:
            messagebox.showinfo("No Solution", "Hill climbing did not find a solution.")

def hill_climbing(initial_state):
    current_state = initial_state.copy()
    max_iterations = 1000
    for _ in range(max_iterations):
        neighbors = generate_neighbors(current_state)
        neighbor_states = [state for state, _ in neighbors]
        neighbor_values = [value for _, value in neighbors]
        best_neighbor_index = min(range(len(neighbor_values)), key=lambda i: neighbor_values[i])
        if neighbor_values[best_neighbor_index] >= evaluate(current_state):
            return current_state
        current_state = neighbor_states[best_neighbor_index]
    return None

def generate_neighbors(state):
    neighbors = []
    empty_tile_index = state.index(0)
    row, col = divmod(empty_tile_index, 3)

    # Move empty tile left
    if col > 0:
        neighbor = state[:]
        neighbor[empty_tile_index], neighbor[empty_tile_index - 1] = neighbor[empty_tile_index - 1], neighbor[empty_tile_index]
        neighbors.append((neighbor, evaluate(neighbor)))

    # Move empty tile right
    if col < 2:
        neighbor = state[:]
        neighbor[empty_tile_index], neighbor[empty_tile_index + 1] = neighbor[empty_tile_index + 1], neighbor[empty_tile_index]
        neighbors.append((neighbor, evaluate(neighbor)))

    # Move empty tile up
    if row > 0:
        neighbor = state[:]
        neighbor[empty_tile_index], neighbor[empty_tile_index - 3] = neighbor[empty_tile_index - 3], neighbor[empty_tile_index]
        neighbors.append((neighbor, evaluate(neighbor)))

    # Move empty tile down
    if row < 2:
        neighbor = state[:]
        neighbor[empty_tile_index], neighbor[empty_tile_index + 3] = neighbor[empty_tile_index + 3], neighbor[empty_tile_index]
        neighbors.append((neighbor, evaluate(neighbor)))

    return neighbors

def evaluate(state):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    return sum(x != y for x, y in zip(state, goal_state))

if __name__ == "__main__":
    root = tk.Tk()
    app = EightPuzzleGUI(root)
    root.mainloop()
