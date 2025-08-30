import tkinter as tk
from tkinter import messagebox
import itertools

# Show all warnings before starting
messagebox.showinfo(
    "⚠ WARNING 1 ⚠",
    "This is a FAKE malware simulator."
)
messagebox.showinfo(
    "⚠ WARNING 2 ⚠",
    "It will flash colors rapidly across your screen in fullscreen."
)
messagebox.showinfo(
    "⚠ WARNING 3 ⚠",
    "⚠ Epilepsy warning ⚠\n"
    "This simulation is SAFE. It does NOT touch your files or harm your computer.\n"
    "Press 'X' on your keyboard to stop the simulation."
)

# Create fullscreen, borderless window
root = tk.Tk()
root.title("Fake Malware Simulator")
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)  # keep on top
root.config(cursor="none")          # hide cursor

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

stop_program = False

# Flashing function
def flash():
    if not stop_program:
        root.configure(bg=next(color_cycle))
        root.after(100, flash)

# Key press handler for only X
def key_press(event):
    global stop_program
    if event.keysym.lower() == 'x':
        stop_program = True
        root.destroy()

# Bind keypress
root.bind("<Key>", key_press)

# Disable window manager close buttons (Alt+F4, close X)
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Start flashing
flash()

# Run GUI loop
root.mainloop()
