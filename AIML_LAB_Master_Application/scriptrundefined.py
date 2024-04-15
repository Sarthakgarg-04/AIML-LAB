import tkinter as tk
from tkinter import messagebox
import subprocess

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Run Script Demo")

        # Create a button to run the script
        self.run_button = tk.Button(root, text="Run Script", command=self.run_script)
        self.run_button.pack(pady=10)

    def run_script(self):
        # Path to the script you want to run
        script_path = "AIML_LAB_Master_Application\AI_Games_Source\exp1.py"

        # Run the script using subprocess
        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to run script: {e}")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
