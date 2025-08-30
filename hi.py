import tkinter as tk
from tkinter import messagebox
import itertools

# Show initial warning
messagebox.showinfo(
    "⚠ WARNING ⚠",
    "This is a FAKE malware simulation.\n"
    "It will flash colors across your screen in fullscreen.\n"
    "⚠ Epilepsy warning ⚠\n"
    "It does NOT touch your files or harm your computer.\n"
    "Press 'X' on your keyboard to stop the simulation at any time."
)

# Create fullscreen window
root = tk.Tk()
root.title("Fake Malware Simulator")
root.attributes('-fullscreen', True)  # covers entire screen
root.config(cursor="none")  # optional: hide cursor for effect

# Instructions label
label = tk.Label(
    root,
    text="Press 'X' to stop the simulation.\nThis is SAFE!",
    font=("Arial", 24),
    fg="white",
    bg="black"
)
label.pack(expand=True)

# Colors for flashing
colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "orange"]
color_cycle = itertools.cycle(colors)

# Stop flag
stop_program = False

# Flashing function
def flash():
    if not stop_program:
        root.configure(bg=next(color_cycle))
        root.after(100, flash)

# Key press handler
def key_press(event):
    global stop_program
    if event.keysym.lower() == 'x':
        stop_program = True
        root.destroy()

# Bind keypress
root.bind("<Key>", key_press)

# Start flashing
flash()

# Run GUI loop
root.mainloop()
