import tkinter as tk
from tkinter import messagebox, simpledialog
import os

# All warnings first
messagebox.showinfo(
    "⚠ Harmless Ransom Simulator ⚠",
    "This is a FAKE ransomware simulator for entertainment and content creation only.\n"
    "It is completely SAFE and does NOT touch your files.\n"
    "Click OK to continue."
)
messagebox.showinfo(
    "⚠ Epilepsy Warning ⚠",
    "The simulation may flash colors or display a fullscreen effect.\n"
    "You must enter the secret code from the ransom note to exit."
)

# Secret code setup
SECRET_CODE = "LETMEOUT"

# Create a fake encryption file (harmless)
fake_file_name = "FAKE_ENCRYPTED_DATA.txt"
with open(fake_file_name, "w") as f:
    f.write("ALL YOUR FILES HAVE BEEN 'ENCRYPTED'!\n")
    f.write("This is completely harmless and for entertainment only.\n")

# Fullscreen window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.config(cursor="none")
root.protocol("WM_DELETE_WINDOW", lambda: None)  # disable Alt+F4

# Ransom note text (includes secret code)
ransom_text = f"""⚠⚠⚠ YOUR FILES HAVE BEEN "ENCRYPTED" ⚠⚠⚠

This is a FAKE ransomware simulator.
Do NOT worry, your files are SAFE.

A fake encrypted file '{fake_file_name}' has been created.

To exit this simulator, type the secret code below:
SECRET CODE: {SECRET_CODE}

For entertainment and content creation purposes only.
"""

# Display ransom note
label = tk.Label(
    root,
    text=ransom_text,
    font=("Courier", 24, "bold"),
    fg="red",
    bg="black",
    justify="center"
)
label.pack(expand=True)

# Full code typing buffer
typed_code = ""

# Key press handler
def key_press(event):
    global typed_code
    global stop_program
    typed_code += event.char.upper()
    # Check if last characters match secret code
    if typed_code[-len(SECRET_CODE):] == SECRET_CODE:
        root.destroy()

root.bind("<Key>", key_press)

# Run GUI loop
root.mainloop()
