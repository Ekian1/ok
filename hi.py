import tkinter as tk
import itertools

# Create main window
root = tk.Tk()
root.title("⚠ WARNING: Fake Malware Simulator ⚠")
root.geometry("600x400")
root.resizable(False, False)

# Epilepsy warning and instructions
label = tk.Label(root, text="⚠ WARNING: This flashes rapidly! ⚠\nPress 'X' on your keyboard to stop.", 
                 font=("Arial", 16), fg="white", bg="black")
label.pack(expand=True)

# Colors for flashing
colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "orange"]
color_cycle = itertools.cycle(colors)

# Flag to stop flashing
stop_program = False

# Flashing function
def flash():
    if not stop_program:
        root.configure(bg=next(color_cycle))
        root.after(100, flash)  # change every 100ms

# Key press handler
def key_press(event):
    global stop_program
    if event.keysym.lower() == 'x':
        stop_program = True
        root.destroy()

# Bind all key presses
root.bind("<Key>", key_press)

# Start flashing
flash()

# Run GUI loop
root.mainloop()
