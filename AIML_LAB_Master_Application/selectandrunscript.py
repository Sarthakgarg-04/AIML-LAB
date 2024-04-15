import tkinter as tk
from tkinter import filedialog
import subprocess

class ScriptRunnerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Script Runner")

        # Create button to select script file
        self.button_select_script = tk.Button(master, text="Select Script", command=self.select_script)
        self.button_select_script.pack(pady=10)

        # Create button to run selected script
        self.button_run_script = tk.Button(master, text="Run Script", command=self.run_script, state=tk.DISABLED)
        self.button_run_script.pack()

        # Create label to display selected script path
        self.label_script_path = tk.Label(master, text="", wraplength=300)
        self.label_script_path.pack(pady=10)

    def select_script(self):
        # Open file dialog to select script file
        script_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if script_path:
            self.script_path = script_path
            self.label_script_path.config(text=f"Selected Script: {script_path}")
            self.button_run_script.config(state=tk.NORMAL)

    def run_script(self):
        # Execute the selected script using subprocess
        if hasattr(self, 'script_path') and self.script_path:
            subprocess.run(['python', self.script_path])
        else:
            tk.messagebox.showerror("Error", "No script selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScriptRunnerApp(root)
    root.mainloop()
