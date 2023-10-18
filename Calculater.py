import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("700x400")
        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.create_ui()

    def create_ui(self):
        style = ttk.Style()
        style.configure("TButton", padding=10, font=("default", 16))
        style.map("TButton",
            foreground=[('pressed', 'black'), ('active', 'blue')],
            background=[('pressed', '!disabled', 'yellow'), ('active', 'lightblue')]
        )

        self.entry = tk.Entry(self.root, textvariable=self.result_var, font=("default, 18"))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row, col = 1, 0
        for button_text in button_texts:
            if button_text == '=':
                btn = ttk.Button(self.root, text=button_text, command=self.calculate)
            elif button_text == 'C':
                btn = ttk.Button(self.root, text=button_text, command=self.clear)
            else:
                btn = ttk.Button(self.root, text=button_text, command=lambda t=button_text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button_text):
        current = self.result_var.get()
        if button_text == 'C':
            self.clear()
        elif button_text == '.':
            if '.' not in current:
                self.result_var.set(current + button_text)
        else:
            self.result_var.set(current + button_text)

    def calculate(self):
        try:
            expression = self.result_var.get()
            result = str(eval(expression))
            self.result_var.set(result)
        except Exception:
            self.result_var.set("Error")

    def clear(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
