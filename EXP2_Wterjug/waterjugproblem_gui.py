import tkinter as tk
from tkinter import messagebox

class WaterJugProblem:
    def __init__(self, master):
        self.master = master
        self.master.title("Water Jug Problem")

        # Initialize jug capacities
        self.jug1_capacity = 5
        self.jug2_capacity = 3

        # Initialize jug levels
        self.jug1_level = 0
        self.jug2_level = 0

        # Create labels for jug capacities
        self.label_jug1 = tk.Label(master, text="5 Gallon Jug")
        self.label_jug1.grid(row=0, column=0)
        self.label_jug2 = tk.Label(master, text="3 Gallon Jug")
        self.label_jug2.grid(row=0, column=2)

        # Create buttons for jug operations
        self.button_fill_jug1 = tk.Button(master, text="Fill", command=self.fill_jug1)
        self.button_fill_jug1.grid(row=1, column=0)
        self.button_fill_jug2 = tk.Button(master, text="Fill", command=self.fill_jug2)
        self.button_fill_jug2.grid(row=1, column=2)

        self.button_empty_jug1 = tk.Button(master, text="Empty", command=self.empty_jug1)
        self.button_empty_jug1.grid(row=2, column=0)
        self.button_empty_jug2 = tk.Button(master, text="Empty", command=self.empty_jug2)
        self.button_empty_jug2.grid(row=2, column=2)

        self.button_pour_jug1_to_jug2 = tk.Button(master, text="Pour Jug 1 to Jug 2", command=self.pour_jug1_to_jug2)
        self.button_pour_jug1_to_jug2.grid(row=3, column=0)
        self.button_pour_jug2_to_jug1 = tk.Button(master, text="Pour Jug 2 to Jug 1", command=self.pour_jug2_to_jug1)
        self.button_pour_jug2_to_jug1.grid(row=3, column=2)

        # Create label for jug levels
        self.label_jug1_level = tk.Label(master, text=f"{self.jug1_level} / {self.jug1_capacity}")
        self.label_jug1_level.grid(row=1, column=1)
        self.label_jug2_level = tk.Label(master, text=f"{self.jug2_level} / {self.jug2_capacity}")
        self.label_jug2_level.grid(row=1, column=3)

    def fill_jug1(self):
        self.jug1_level = self.jug1_capacity
        self.update_labels()

    def fill_jug2(self):
        self.jug2_level = self.jug2_capacity
        self.update_labels()

    def empty_jug1(self):
        self.jug1_level = 0
        self.update_labels()

    def empty_jug2(self):
        self.jug2_level = 0
        self.update_labels()

    def pour_jug1_to_jug2(self):
        amount_to_pour = min(self.jug1_level, self.jug2_capacity - self.jug2_level)
        self.jug1_level -= amount_to_pour
        self.jug2_level += amount_to_pour
        self.update_labels()

    def pour_jug2_to_jug1(self):
        amount_to_pour = min(self.jug2_level, self.jug1_capacity - self.jug1_level)
        self.jug2_level -= amount_to_pour
        self.jug1_level += amount_to_pour
        self.update_labels()

    def update_labels(self):
        self.label_jug1_level.config(text=f"{self.jug1_level} / {self.jug1_capacity}")
        self.label_jug2_level.config(text=f"{self.jug2_level} / {self.jug2_capacity}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WaterJugProblem(root)
    root.mainloop()
