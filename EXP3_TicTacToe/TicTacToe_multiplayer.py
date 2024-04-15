import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")

        # Initialize variables
        self.current_player = "X"
        self.board = [[""]*3 for _ in range(3)]  # Initialize empty board
        self.game_over = False

        # Create buttons for the game board
        self.buttons = [[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text="", font=("Arial", 20), width=6, height=3,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

    def on_button_click(self, row, col):
        # Handle button click event
        if not self.game_over and self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(row, col):
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.game_over = True
            elif self.check_draw():
                messagebox.showinfo("Draw", "It's a draw!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, row, col):
        # Check if the current player has won
        symbol = self.board[row][col]
        # Check row
        if all(self.board[row][i] == symbol for i in range(3)):
            return True
        # Check column
        if all(self.board[i][col] == symbol for i in range(3)):
            return True
        # Check diagonal
        if row == col and all(self.board[i][i] == symbol for i in range(3)):
            return True
        # Check anti-diagonal
        if row + col == 2 and all(self.board[i][2-i] == symbol for i in range(3)):
            return True
        return False

    def check_draw(self):
        # Check if the game is a draw
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
