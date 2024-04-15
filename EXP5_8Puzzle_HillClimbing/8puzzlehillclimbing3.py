import tkinter as tk
from tkinter import messagebox
import random

class EightPuzzleGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("8 Puzzle")
        self.master.geometry("400x300")
        
        # Generate random initial state and goal state
        self.initial_state = self.generate_random_state()
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, None]]

        # Display initial state and goal state
        self.initial_label = tk.Label(master, text="Initial State:")
        self.initial_label.pack()
        self.display_state(self.initial_state)

        self.goal_label = tk.Label(master, text="Goal State:")
        self.goal_label.pack()
        self.display_state(self.goal_state)

        # Solve button
        self.solve_button = tk.Button(master, text="Solve", command=self.solve_puzzle)
        self.solve_button.pack()

    def generate_random_state(self):
        # Generate a random initial state for the puzzle
        nums = list(range(1, 9))
        random.shuffle(nums)
        state = [[nums.pop(0) for _ in range(3)] for _ in range(3)]
        state[2][2] = None  # Empty tile
        return state

    def display_state(self, state):
        # Display the state of the puzzle
        for row in state:
            print(row)

    def solve_puzzle(self):
        # Solve the puzzle using hill climbing algorithm
        current_state = self.initial_state
        moves = []
        while not self.is_goal_state(current_state):
            # Implement your hill climbing algorithm here
            # For demonstration purposes, just swap empty tile with a random adjacent tile
            empty_pos = self.find_empty_tile(current_state)
            neighbors = self.get_valid_neighbors(current_state, empty_pos)
            random_neighbor = random.choice(neighbors)
            current_state[empty_pos[0]][empty_pos[1]] = current_state[random_neighbor[0]][random_neighbor[1]]
            current_state[random_neighbor[0]][random_neighbor[1]] = None
            moves.append(random_neighbor)
            self.display_state(current_state)
            self.master.update()
            self.master.after(1000)  # Delay for visualization

        messagebox.showinfo("Solved", f"Puzzle solved in {len(moves)} moves.")

    def is_goal_state(self, state):
        # Check if the current state is the goal state
        return state == self.goal_state

    def find_empty_tile(self, state):
        # Find the coordinates of the empty tile
        for i in range(3):
            for j in range(3):
                if state[i][j] is None:
                    return (i, j)

    def get_valid_neighbors(self, state, pos):
        # Get valid neighbors of the empty tile
        neighbors = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            new_x, new_y = pos[0] + dx, pos[1] + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                neighbors.append((new_x, new_y))
        return neighbors


if __name__ == "__main__":
    root = tk.Tk()
    app = EightPuzzleGUI(root)
    root.mainloop()
