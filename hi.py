import tkinter as tk
from tkinter import messagebox
import os
import shutil

# --- Step 1: Warnings ---
def show_warnings():
    messagebox.showinfo(
        "⚠ Harmless Ransom Simulator ⚠",
        "This is a FAKE ransomware simulator for entertainment/content creation only.\n"
        "It is completely SAFE and does NOT delete or harm your files."
    )
    messagebox.showinfo(
        "⚠ Epilepsy Warning ⚠",
        "The simulation may flash colors or display a fullscreen effect.\n"
        "You must type the secret code from the ransom note to exit."
    )

show_warnings()  # Only proceed after clicking OK twice

# --- Step 2: Setup ---
SECRET_CODE = "LETMEOUT"  # Code shown only in ransom note
ENCRYPTION_FOLDER = "ENCRYPTION"
os.makedirs(ENCRYPTION_FOLDER, exist_ok=True)

# Copy files into "encrypted" folder (safe)
for file in os.listdir():
    if os.path.isfile(file) and file != os.path.basename(__file__):
        shutil.copy(file, os.path.join(ENCRYPTION_FOLDER, file))

# --- Step 3: Fullscreen Ransom Note ---
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

# --- Step 4: Secret code typing logic ---
typed_code = ""

def key_press(event):
    global typed_code
    typed_code += event.char.upper()
    if typed_code[-len(SECRET_CODE):] == SECRET_CODE:
        root.destroy()

root.bind("<Key>", key_press)

# --- Step 5: Run GUI loop ---
root.mainloop()
