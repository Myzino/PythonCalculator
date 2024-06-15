import tkinter as tk
from function import add, subtract, multiply, divide
from scientific import Tan, Sin, Cos

class Calculator:
    def __init__(gui, root):
        gui.root = root
        gui.root.title("Calculator")
        
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
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 3), ('Tan', 4, 2),
            ('CA', 5, 0), ('C', 5, 1), ('Sin', 5, 2), ('Cos', 5, 3),
            ('=', 6, 0)
        ]

        for (text, row, col) in buttons:
            gui.create_button(text, row, col)
        
        for i in range(7):
            gui.frame.rowconfigure(i, weight=1)
        for j in range(4):
            gui.frame.columnconfigure(j, weight=1)

    def create_button(gui, text, row, col):
        button = tk.Button(gui.frame, text=text, padx=20, pady=20, font=('Arial', 18),
                           command=lambda: gui.on_button_click(text))
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
                    'Tan': Tan,
                    'Sin': Sin,
                    'Cos': Cos
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
