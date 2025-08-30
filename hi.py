import tkinter as tk
from tkinter import simpledialog, messagebox

# Secret code setup
SECRET_CODE = "LETMEOUT"

# Initial warning and code prompt
messagebox.showinfo(
    "⚠ Harmless Ransom Simulator ⚠",
    "This is a FAKE ransom simulator for entertainment/content creation only.\n"
    "It is completely SAFE and does NOT touch any files.\n"
    "To stop the simulation, you must enter a secret code."
)

# Ask user to enter the code
code_input = simpledialog.askstring(
    "Enter Secret Code",
    "Enter the secret code to allow closing the simulator later:"
)

if code_input != SECRET_CODE:
    messagebox.showinfo(
        "Wrong Code",
        "You entered the wrong code. The simulation will still run, "
        "but you must enter the correct code to stop it."
    )

# Create fullscreen, borderless window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.config(cursor="none")

# Disable all other close events
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Fake ransom text
ransom_text = """⚠⚠⚠ YOUR FILES HAVE BEEN "ENCRYPTED" ⚠⚠⚠

This is a FAKE ransom simulator.
Do NOT worry, your files are SAFE.

You must enter the secret code from the warning to exit.
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

# Key press handler: only closes if correct code typed
def key_press(event):
    global stop_program
    typed = event.char.upper()
    if typed == SECRET_CODE[0]:  # check first letter as a hint
        # Optionally you could implement full code typing check here
        stop_program = True
        root.destroy()

# Bind keypress (full code check is optional; currently just placeholder)
root.bind("<Key>", key_press)

# Run GUI loop
root.mainloop()
