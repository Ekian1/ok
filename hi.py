import tkinter as tk
import itertools
from pynput import keyboard

# Global stop flag
stop_program = False

# Function to handle keypresses
def on_press(key):
    global stop_program
    try:
        if key.char.lower() == 'x':  # Press X to stop
            stop_program = True
            root.destroy()
    except AttributeError:
        pass

# Start keyboard listener
from pynput import keyboard
listener = keyboard.Listener(on_press=on_press)
listener.start()

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

# Function to flash background
def flash():
    if not stop_program:
        root.configure(bg=next(color_cycle))
        root.after(100, flash)

flash()
root.mainloop()
listener.stop()
