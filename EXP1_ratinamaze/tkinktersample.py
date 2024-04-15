import tkinter as tk
from tkinter import messagebox

def greet():
    messagebox.showinfo("Greeting", "Hello, " + name.get() + "!")

# Create the main window
root = tk.Tk()
root.title("Greeting App")

# Create a label
label = tk.Label(root, text="Enter your name:")
label.pack()

# Create an entry field
name = tk.StringVar()
entry = tk.Entry(root, textvariable=name)
entry.pack()

# Create a button
button = tk.Button(root, text="Greet", command=greet)
button.pack()

# Run the application
root.mainloop()
