import tkinter as tk
from tkinter import simpledialog
import random
import string

def generate_password():
    length = simpledialog.askinteger("Password Length", "Enter password length:")
    if length is None:
        return

    include_uppercase = simpledialog.askstring("Include Uppercase", "Include uppercase letters? (y/n):").lower() == 'y'
    include_lowercase = simpledialog.askstring("Include Lowercase", "Include lowercase letters? (y/n):").lower() == 'y'
    include_digits = simpledialog.askstring("Include Digits", "Include digits? (y/n):").lower() == 'y'
    include_special = simpledialog.askstring("Include Special Characters", "Include special characters? (y/n):").lower() == 'y'

    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Generate Password Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Run the main event loop
root.mainloop()
