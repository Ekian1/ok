import tkinter as tk
import itertools

# Create window
root = tk.Tk()
root.title("Fake Malware")
root.geometry("500x500")
root.resizable(False, False)

# Colors to flash
colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]
color_cycle = itertools.cycle(colors)

# Function to change background color
def flash():
    root.configure(bg=next(color_cycle))
    root.after(100, flash)  # change every 100ms

# Start flashing
flash()

# Start GUI loop
root.mainloop()
