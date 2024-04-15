import tkinter as tk
from tkinter import messagebox
import subprocess

class ExperimentDashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Experiment Dashboard")

        # Experiment descriptions
        self.experiment_descriptions = {
            "Experiment 1": "Description of Experiment 1",
            "Experiment 2": "Description of Experiment 2",
            "Experiment 3": "Description of Experiment 3",
            "Experiment 4": "Description of Experiment 4",
            "Experiment 5": "Description of Experiment 5",
            "Experiment 6": "Description of Experiment 6",
            "Experiment 7": "Description of Experiment 7"
        }

        # Script paths for each experiment
        self.script_paths = {
            "Experiment 1": "exp1.py",
            "Experiment 2": "AIML_LAB_Master_Application/AI_Games_Source/2_waterjug.py",
            "Experiment 3": "AIML_LAB_Master_Application/AI_Games_Source/3_TicTacToe_multiplayer.py",
            "Experiment 4": "AIML_LAB_Master_Application/AI_Games_Source/4_8puzzle.py",
            "Experiment 5": "path_to_experiment_5_script.py",
            "Experiment 6": "path_to_experiment_6_script.py",
            "Experiment 7": "path_to_experiment_7_script.py"
        }

        # Create experiment buttons
        self.create_experiment_buttons()

    def create_experiment_buttons(self):
        for experiment in self.experiment_descriptions:
            button = tk.Button(self.master, text=experiment, command=lambda exp=experiment: self.run_experiment(exp))
            button.pack(pady=5)

    def run_experiment(self, experiment):
        script_path = self.script_paths.get(experiment)
        if script_path:
            try:
                subprocess.run(["python", script_path], check=True)
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to run script: {e}")
        else:
            messagebox.showerror("Error", "Script path not found for the selected experiment.")

def main():
    root = tk.Tk()
    app = ExperimentDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
