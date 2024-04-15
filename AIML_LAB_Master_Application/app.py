import tkinter as tk
from tkinter import messagebox
import os
class ExperimentDashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("AIML GUI Dashboard")
        self.master.geometry("720x720")
        self.label_heading = tk.Label(master, text="Experiment Dashboard", font=("Arial", 16, "bold"))
        self.label_heading.pack(pady=10)
        self.label_heading = tk.Label(master, text="List of Experiments", font=("Arial", 12))
        self.label_heading.pack()
        experiments = {
            "Lab1": "AIML_LAB_Master_Application\AI_Games_Source\exp1.py",
            "Lab2": "Lab2.py",
            "Lab3": "Lab3.py",
            "Lab4": "Lab4.py",
            "Lab5": "Lab5.py",
            "Lab6": "Lab6.py",
            "Lab7": "Lab7.py",
            "Lab8": "Lab8.py"
        }
        self.label_info = tk.Label(master, text="Tanishq Vijay, 219302307\nIT-6B",font=("Arial",10))
        self.label_info.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)
        for experiment, script_name in experiments.items():
            button = tk.Button(master, text=experiment, command=lambda script=script_name: self.run_experiment(script))
            button.pack(fill=tk.X, padx=10, pady=5)
            button.config(cursor="hand2")
    def run_experiment(self, script_name):
        script_path = f"C:/Users/{os.getlogin()}/Desktop/AIML Lab/{script_name}"
        if os.path.isfile(script_path):
            os.system(f"python \"{script_path}\"")
        else:
            messagebox.showerror("Error", f"No Python script found for {script_name}.")
if __name__ == "__main__":
    root = tk.Tk()
    app = ExperimentDashboard(root)
    root.mainloop()