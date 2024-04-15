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
            "Maze_Solver": "MazeSolver:\n\n Click a tile to add an obstacle.Upon placing an obstacle the tile turns from green to red, place tiles on the desired positions and click of find path button to view results of the maze solver mini-application",
            "Water_Jug ": "Water Jug Problem:\n\nEnter the capacity of the two water jugs, all the steps involved thereafter are automated and willapppear as we close the pop-up window.",
            "Tic_Tac_Toe": "TicTacToe:\n\nA blank GUI grid is displayed, User plays X first and computer automatically plays O second,Moves are played until a result is achieved which is displayed in a pop up window. ",
            "8_Puzzle_Problem": "8 Puzzle Problem:\n\nclick on Set Initial state button to set an initial state, use the Up Down Left and Right button to move the 0 tile to achieve the Goal state displayed on the side.The moves taken to achieve the goal state are counted and updated at each step.\nA succesful completion message is displayed once the goal state is sachieved.",
            # "Experiment 5": "Description of Experiment 5:\n\n[Add your Experiment 5 description here.]",
            # "Experiment 6": "Description of Experiment 6:\n\n[Add your Experiment 6 description here.]",
            # "Experiment 7": "Description of Experiment 7:\n\n[Add your Experiment 7 description here.]"
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

        #Script path variables for the experiments
        script_path1 = "AIML_LAB_Master_Application\AI_Games_Source\exp1.py"
        script_path2 = "AIML_LAB_Master_Application\AI_Games_Source\exp2.py"
        script_path3 = "AIML_LAB_Master_Application\AI_Games_Source\exp3_singleplayer.py"
        script_path4 = "AIML_LAB_Master_Application\AI_Games_Source\exp4.py"

        # Run the script using subprocess
        # try:
        #     subprocess.run(["python", script_path1], check=True)
        # except subprocess.CalledProcessError as e:
        #     messagebox.showerror("Error", f"Failed to run script: {e}")


        # if selected_experiment:
        if selected_experiment == "Maze_Solver":
            try:    
                subprocess.run(["python", script_path1], check=True)
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to run script: {e}")

        elif selected_experiment == "Maze_Solver":
            try:    
                subprocess.run(["python", script_path2], check=True)
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to run script: {e}")

        elif selected_experiment == "Tic_Tac_Toe":
            try:    
                subprocess.run(["python", script_path3], check=True)
            except subprocess.CalledProcessError as e:
                 messagebox.showerror("Error", f"Failed to run script: {e}")

        elif selected_experiment == "8_Puzzle_Problem":
            try:    
                subprocess.run(["python", script_path4], check=True)
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to run script: {e}")                        
            
        else:
                messagebox.showerror("Error", "Python script not found for the selected experiment.")
        # else:
        #     messagebox.showerror("Error", "Please select an experiment first.")


    # def conduct_experiment(self):
    #     script_path1 = "AIML_LAB_Master_Application\AI_Games_Source\exp1.py"
    #     selected_experiment = ""
    #     for button in self.buttons:
    #         if button['state'] == tk.ACTIVE:
    #             selected_experiment = button['text']
    #             break
    #     if selected_experiment == "Maze_Solver":
    #         # script_path1 = "AIML_LAB_Master_Application\AI_Games_Source\exp1.py"
    #         try:
    #             subprocess.run(["python", script_path1], check=True)
    #         except subprocess.CalledProcessError as e:
    #             messagebox.showerror("Error", f"Failed to run script: {e}")
        
    #         # if selected_experiment == "Maze_Solver":
    #         #     script_path1 = "AIML_LAB_Master_Application\AI_Games_Source\exp1.py"
    #         #     subprocess.run(['python', script_path1])
                
    #         # elif selected_experiment == "Water_Jug":
    #         #     script_path2 = "AIML_LAB_Master_Application\AI_Games_Source\exp2.py"
    #         #     subprocess.run(['python', script_path2])
    #         # else:
    #         #     messagebox.showerror("Error", "Python script not found for the selected experiment.")
    #     else:
    #         messagebox.showerror("Error", "Please select an experiment first.")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = ExperimentDashboard(root)
    root.mainloop()
