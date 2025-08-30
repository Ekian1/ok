import tkinter as tk
from tkinter import messagebox

# Initial confirmation
confirm = messagebox.askyesno(
    "⚠ Harmless Ransom Simulator ⚠",
    "This is a FAKE ransom simulator for entertainment/content creation only.\n"
    "It will show a fake ransom note on your screen.\n\n"
    "It is completely SAFE and does NOT touch any files.\n"
    "Do you want to run it?"
)

if not confirm:
    exit()  # User chose not to run

# Create fullscreen, borderless window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.config(cursor="none")  # Hide cursor for effect

# Disable all other close events
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Fake ransom text
ransom_text = """⚠⚠⚠ YOUR FILES HAVE BEEN "ENCRYPTED" ⚠⚠⚠

This is a FAKE ransom simulator.
Do NOT worry, your files are SAFE.

Press 'X' on your keyboard to exit at any time.
For entertainment and content creation purposes only.
"""

# Label to display the text
label = tk.Label(
    root,
    text=ransom_text,
    font=("Courier", 24, "bold"),
    fg="red",
    bg="black",
    justify="center"
)
label.pack(expand=True)

# Stop flag
stop_program = False

# Key press handler for only X
def key_press(event):
    global stop_program
    if event.keysym.lower() == 'x':
        stop_program = True
        root.destroy()

# Bind keypress
root.bind("<Key>", key_press)

# Run GUI loop
root.mainloop()
