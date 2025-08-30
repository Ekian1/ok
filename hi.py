import tkinter as tk
from tkinter import messagebox
import os
import shutil

# --- Warnings before running ---
messagebox.showinfo(
    "⚠ Harmless Ransom Simulator ⚠",
    "This is a FAKE ransomware simulator for entertainment/content creation only.\n"
    "It is completely SAFE and does NOT delete or harm your files.\n"
    "Click OK to continue."
)
messagebox.showinfo(
    "⚠ Epilepsy Warning ⚠",
    "The simulation may flash colors or display a fullscreen effect.\n"
    "You must type the secret code from the ransom note to exit."
)

# --- Setup ---
SECRET_CODE = "LETMEOUT"  # Code shown only inside ransom note

# Create folder for fake encryption
ENCRYPTION_FOLDER = "ENCRYPTION"
os.makedirs(ENCRYPTION_FOLDER, exist_ok=True)

# List files in current directory (safe demo)
for file in os.listdir():
    if os.path.isfile(file) and file != os.path.basename(__file__):
        # Move file to encryption folder (harmless, just moves a copy)
        shutil.copy(file, os.path.join(ENCRYPTION_FOLDER, file))

# --- Fullscreen Ransom Note ---
root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.config(cursor="none")
root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable Alt+F4

ransom_text = f"""⚠⚠⚠ YOUR FILES HAVE BEEN "ENCRYPTED" ⚠⚠⚠

This is a FAKE ransomware simulator.
Do NOT worry, your files are SAFE.

All your files have been copied to the folder '{ENCRYPTION_FOLDER}'.
They were NOT deleted or harmed.

To exit this simulator, type the secret code below:
SECRET CODE: {SECRET_CODE}

For entertainment and content creation purposes only.
"""

label = tk.Label(
    root,
    text=ransom_text,
    font=("Courier", 24, "bold"),
    fg="red",
    bg="black",
    justify="center"
)
label.pack(expand=True)

# --- Full code typing logic ---
typed_code = ""

def key_press(event):
    global typed_code
    typed_code += event.char.upper()
    if typed_code[-len(SECRET_CODE):] == SECRET_CODE:
        root.destroy()

root.bind("<Key>", key_press)

root.mainloop()
