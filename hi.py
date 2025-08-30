import tkinter as tk
from tkinter import simpledialog, messagebox
import os

# Secret code
SECRET_CODE = "LETMEOUT"

# Warning before running
messagebox.showinfo(
    "⚠ Harmless Ransom Simulator ⚠",
    "This is a FAKE ransomware simulator for entertainment and content creation only.\n"
    "It is completely SAFE, does NOT delete or harm files.\n"
    "You will be asked for a secret code to exit."
)

# Ask user to input the secret code for closing later
code_input = simpledialog.askstring(
    "Enter Secret Code",
    "Enter a secret code that will be required to close the simulator later:"
)

if not code_input:
    messagebox.showinfo("Cancelled", "You cancelled the simulation. Exiting.")
    exit()

# Create fake encryption file
fake_file_name = "FAKE_ENCRYPTED_DATA.txt"
with open(fake_file_name, "w") as f:
    f.write("ALL YOUR FILES HAVE BEEN 'ENCRYPTED'!\n")
    f.write("This is a harmless simulation for entertainment only.\n")
    f.write(f"The secret code to stop the simulation is: {SECRET_CODE}\n")

# Create fullscreen window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.config(cursor="none")
root.protocol("WM_DELETE_WINDOW", lambda: None)  # disable Alt+F4

# Ransom note text
ransom_text = f"""⚠⚠⚠ YOUR FILES HAVE BEEN "ENCRYPTED" ⚠⚠⚠

This is a FAKE ransomware simulator.
Do NOT worry, your files are SAFE.
A fake encrypted file '{fake_file_name}' has been created.

Enter the secret code to exit: {SECRET_CODE}
For entertainment and content creation only.
"""

# Display label
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

# Key press handler: only closes with the secret code
def key_press(event):
    global stop_program
    typed = event.char
    # Simple full code check (for demonstration, press first letter to close)
    if typed.upper() == SECRET_CODE[0]:  
        # Optional: implement full typing for extra realism
        stop_program = True
        root.destroy()

root.bind("<Key>", key_press)

# Run GUI loop
root.mainloop()
