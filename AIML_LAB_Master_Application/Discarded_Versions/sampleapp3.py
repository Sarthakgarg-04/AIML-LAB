import tkinter as tk
import subprocess

class ScriptRunnerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Script Runner")

        # Predefined path to the Python script
        self.script_path = "C:\Users\91997\Downloads\AIML_Lab\EXP1_Ratinamaze\ ratinamaze_GUI.py"

        # Create button to run predefined script
        self.button_run_script = tk.Button(master, text="Run Script", command=self.run_script)
        self.button_run_script.pack(pady=10)

        # Create label to display predefined script path
        self.label_script_path = tk.Label(master, text=f"Predefined Script: {self.script_path}", wraplength=300)
        self.label_script_path.pack(pady=10)

    def run_script(self):
        # Execute the predefined script using subprocess
        subprocess.run(['python', self.script_path])

if __name__ == "__main__":
    root = tk.Tk()
    app = ScriptRunnerApp(root)
    root.mainloop()
