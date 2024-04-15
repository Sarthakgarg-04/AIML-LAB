import tkinter as tk
import heapq

class PuzzleGUI:
    def __init__(self, master, initial_state):
        self.master = master
        self.master.title("8 Puzzle Problem")
        self.master.geometry("300x400")

        self.canvas = tk.Canvas(master, width=300, height=300, borderwidth=2, relief="ridge")
        self.canvas.pack()

        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
        self.empty_pos = self.find_empty_tile(initial_state)
        self.tiles = []

        self.draw_tiles()

        solve_button = tk.Button(master, text="Solve", command=self.solve_puzzle)
        solve_button.pack()

    def draw_tiles(self):
        self.tiles.clear()
        for i in range(3):
            for j in range(3):
                tile_value = self.initial_state[i][j]
                x1, y1 = j * 100, i * 100
                x2, y2 = x1 + 100, y1 + 100
                tile = self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")
                self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=str(tile_value) if tile_value is not None else "",
                                        font=("Arial", 24, "bold"))
                self.tiles.append(tile)

    def find_empty_tile(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] is None:
                    return (i, j)

    def move_tile(self, i, j):
        if abs(self.empty_pos[0] - i) + abs(self.empty_pos[1] - j) == 1:
            self.initial_state[self.empty_pos[0]][self.empty_pos[1]] = self.initial_state[i][j]
            self.initial_state[i][j] = None
            self.empty_pos = (i, j)
            self.draw_tiles()

    def solve_puzzle(self):
        goal_state_flat = [1, 2, 3, 4, 5, 6, 7, 8, None]

        open_set = [(self.heuristic(self.initial_state, goal_state_flat), self.initial_state)]
        heapq.heapify(open_set)
        closed_set = set()

        while open_set:
            _, current_state = heapq.heappop(open_set)

            if self.is_goal_state(current_state):
                self.initial_state = current_state
                self.draw_tiles()
                return

            closed_set.add(tuple(map(tuple, current_state)))

            for successor in self.successors(current_state):
                if tuple(map(tuple, successor)) not in closed_set:
                    heapq.heappush(open_set, (self.heuristic(successor, goal_state_flat), successor))

    def heuristic(self, state, goal_state_flat):
        state_flat = [val for row in state for val in row]
        return sum(s != g for s, g in zip(state_flat, goal_state_flat))

    def is_goal_state(self, state):
        return state == self.goal_state

    def successors(self, state):
        successors = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = self.empty_pos[0] + dx, self.empty_pos[1] + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [row[:] for row in state]
                new_state[self.empty_pos[0]][self.empty_pos[1]] = new_state[new_x][new_y]
                new_state[new_x][new_y] = None
                successors.append(new_state)
        return successors


if __name__ == "__main__":
    initial_state = [[1, 2, 3], [4, None, 6], [7, 5, 8]]

    root = tk.Tk()
    app = PuzzleGUI(root, initial_state)
    root.mainloop()
