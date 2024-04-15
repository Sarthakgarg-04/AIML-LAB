import tkinter as tk
from tkinter import messagebox
import subprocess

class ExperimentDashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("AIML Lab Experiments Application")

        # Create heading
        self.label_heading = tk.Label(master, text="AIML Lab Experiments Application", font=("Arial", 16, "bold"))
        self.label_heading.pack(pady=10)

        # Create index on the left
        self.frame_index = tk.Frame(master)
        self.frame_index.pack(side=tk.LEFT, padx=10, pady=10)

        self.experiments = {
            "MazeSolver": "MazeSolver:\n\n Click a tile to add an obstacle.Upon placing an obstacle the tile turns from green to red, place tiles on the desired positions and click of find path button to view results of the maze solver mini-application",
            "Experiment 2": "Description of Experiment 2:\n\n[Add your Experiment 2 description here.]",
            "Experiment 3": "Description of Experiment 3:\n\n[Add your Experiment 3 description here.]",
            "Experiment 4": "Description of Experiment 4:\n\n[Add your Experiment 4 description here.]",
            "Experiment 5": "Description of Experiment 5:\n\n[Add your Experiment 5 description here.]",
            "Experiment 6": "Description of Experiment 6:\n\n[Add your Experiment 6 description here.]",
            "Experiment 7": "Description of Experiment 7:\n\n[Add your Experiment 7 description here.]"
        }

        self.buttons = []
        for experiment in self.experiments:
            button = tk.Button(self.frame_index, text=experiment, command=lambda exp=experiment: self.show_description(exp))
            button.pack(fill=tk.X, padx=10, pady=5)
            self.buttons.append(button)

        # Create main screen to display description and conduct experiment button
        self.frame_main = tk.Frame(master)
        self.frame_main.pack(side=tk.LEFT, padx=10, pady=10)

        self.label_description = tk.Label(self.frame_main, text="Select an experiment from the index to view its description.")
        self.label_description.pack(pady=10)

        self.button_conduct = tk.Button(self.frame_main, text="Conduct Experiment", command=self.conduct_experiment, state=tk.ACTIVE)
        self.button_conduct.pack()

        # Create footnote on the bottom
        self.label_footnote = tk.Label(master, text="Submitted By: Sarthak Garg - 219302116 -IT6B \n For evaluation of AIML Lab (IT2131)", font=("Arial", 8))
        self.label_footnote.pack(side=tk.BOTTOM, pady=10)

    def show_description(self, experiment):
        description = self.experiments.get(experiment, "Description not available.")
        self.label_description.config(text=description)
        self.button_conduct.config(state=tk.NORMAL)

    def conduct_experiment(self):
        selected_experiment = ""
        for button in self.buttons:
            if button['state'] == tk.ACTIVE:
                selected_experiment = button['text']
                break
        if selected_experiment:
            subprocess.run(['python', f'{selected_experiment}.py'])
        else:
            messagebox.showerror("Error", "Please select an experiment first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExperimentDashboard(root)
    root.mainloop()
