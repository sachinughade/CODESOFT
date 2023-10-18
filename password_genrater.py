import random
import string
import tkinter as tk
import customtkinter

class PassGen:
    def __init__(self, root):
        self.root = root
        self.root.title("Password")
        self.create_widgets()

    def create_widgets(self):

        self.length_label = customtkinter.CTkLabel(self.root, text="Length of password:")
        self.length_label.pack()

        self.length_entry = customtkinter.CTkEntry(self.root)
        self.length_entry.pack()


        self.use_uppercase_var = tk.BooleanVar()
        self.use_uppercase_var.set(True)
        self.uppercase_check = customtkinter.CTkCheckBox(self.root, text="Uppercase Letters", variable=self.use_uppercase_var)
        self.uppercase_check.pack()
        self.use_lowercase_var = tk.BooleanVar()
        self.use_lowercase_var.set(True)
        self.lowercase_check = customtkinter.CTkCheckBox(self.root, text="Lowercase Letters", variable=self.use_lowercase_var)
        self.lowercase_check.pack()

        # Create and pack the checkbox for digits
        self.use_digits_var = tk.BooleanVar()
        self.use_digits_var.set(True)
        self.digits_check = customtkinter.CTkCheckBox(self.root, text="Digits", variable=self.use_digits_var)
        self.digits_check.pack()

        self.use_special_var = tk.BooleanVar()
        self.use_special_var.set(False)
        self.special_check = customtkinter.CTkCheckBox(self.root, text="Special Characters", variable=self.use_special_var)
        self.special_check.pack()

        # Create and pack the label for the number of passwords to generate
        self.count_label = customtkinter.CTkLabel(self.root, text="Number of Passwords:")
        self.count_label.pack()

        # Create and pack the entry field for the number of passwords to generate
        self.count_entry = customtkinter.CTkEntry(self.root)
        self.count_entry.pack()

        # Create and pack the "Generate" button and associate it with the generate_passwords method
        self.generate_button = customtkinter.CTkButton(self.root, text="Generate", command=self.generate_passwords)
        self.generate_button.pack()

        # Create and pack the textbox to display generated passwords
        self.generated_passwords_text = customtkinter.CTkTextbox(self.root, height=150, width=250)
        self.generated_passwords_text.pack()

    def generate_passwords(self):
        length = int(self.length_entry.get())  # Get the selected password length
        use_uppercase = self.use_uppercase_var.get()  # Get the checkbox state for uppercase letters
        use_lowercase = self.use_lowercase_var.get()  # Get the checkbox state for lowercase letters
        use_digits = self.use_digits_var.get()  # Get the checkbox state for digits
        use_special = self.use_special_var.get()  # Get the checkbox state for special characters
        count = int(self.count_entry.get())  # Get the number of passwords to generate

        characters = ""
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        passwords = []
        for _ in range(count):
            password = ''.join(random.choice(characters) for _ in range(length))
            if use_special:
                if len(password) > 1:
                    password = password[:1] + random.choice(string.punctuation) + password[1:]
            passwords.append(password)

        passwords_text = "\n".join(passwords)
        self.generated_passwords_text.delete(1.0, tk.END)
        self.generated_passwords_text.insert(tk.END, passwords_text)

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = PassGen(root)
    root.mainloop()

