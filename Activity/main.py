import tkinter as tk
from function import add, subtract, multiply, divide
from scientific import Tan, Sin, Cos

class Calculator:
    def __init__(gui, root):
        gui.root = root
        gui.root.title("Trigonometry Calculator")
        
        gui.root.rowconfigure(0, weight=1)
        gui.root.columnconfigure(0, weight=1)
        
        gui.create_ui()

    def create_ui(gui):
        
        gui.frame = tk.Frame(gui.root)
        gui.frame.grid(sticky="nsew")
        
        gui.frame.rowconfigure(0, weight=1)
        gui.frame.columnconfigure(0, weight=1)
        
        gui.entry = tk.Entry(gui.frame, font=('Arial', 24), bd=8, insertwidth=1)
        gui.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ('CA', 1, 0, 'red'), ('C', 1, 1, 'red'), ('Sin', 1, 2, 'blue'), ('Cos', 1, 3, 'blue'),
            ('7', 2, 0, 'lightgray'), ('8', 2, 1, 'lightgray'), ('9', 2, 2, 'lightgray'), ('Tan', 2, 3, 'blue'),
            ('4', 3, 0, 'lightgray'), ('5', 3, 1, 'lightgray'), ('6', 3, 2, 'lightgray'), ('/', 3, 3, 'orange'),
            ('1', 4, 0, 'lightgray'), ('2', 4, 1, 'lightgray'), ('3', 4, 2, 'lightgray'), ('*', 4, 3, 'orange'),
            ('0', 5, 0, 'lightgray'), ('.', 5, 1, 'lightgray'), ('+', 5, 3, 'orange'), ('-', 5, 2, 'orange'),
            ('=', 6, 0, 'green')
        ]

        for (text, row, col, color) in buttons:
            gui.create_button(text, row, col, color)
        
        for i in range(7):
            gui.frame.rowconfigure(i, weight=1)
        for j in range(4):
            gui.frame.columnconfigure(j, weight=1)

    def create_button(gui, text, row, col, color):
        button = tk.Button(gui.frame, text=text, padx=20, pady=20, font=('Arial', 18),
                           bg=color, command=lambda: gui.on_button_click(text))
        button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(gui, char):
        if char == '=':
            try:
                expression = gui.entry.get()
                result = eval(expression, {'__builtins__': None}, { 
                    'add': add,
                    'subtract': subtract,
                    'multiply': multiply,
                    'divide': divide,
                    'Tan' : Tan,
                    'Sin' : Sin,
                    'Cos': Cos,
                })
                gui.entry.delete(0, tk.END)
                gui.entry.insert(tk.END, str(result))
            except Exception as e:
                gui.entry.delete(0, tk.END)
                gui.entry.insert(tk.END, "Error")
        elif char in ['CA', 'C']:
            if char == 'CA':
                gui.entry.delete(0, tk.END)
            elif char == 'C':
                current_text = gui.entry.get()
                if current_text:
                    new_text = current_text[:-1]
                    gui.entry.delete(0, tk.END)
                    gui.entry.insert(tk.END, new_text)
        elif char in ['Sin', 'Cos', 'Tan']:
            current_text = gui.entry.get()
            new_text = f"{char}({current_text})"
            gui.entry.delete(0, tk.END)
            gui.entry.insert(tk.END, new_text)
        else:
            current_text = gui.entry.get()
            new_text = current_text + str(char)
            gui.entry.delete(0, tk.END)
            gui.entry.insert(tk.END, new_text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
