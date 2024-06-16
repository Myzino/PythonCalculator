import tkinter as tk
from function import add, subtract, multiply, divide


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
            ('CA', 1, 0, 'red'), ('C', 1, 1, 'red'), ('', 1, 2, 'gray'), ('', 1, 3, 'gray'),
            ('7', 2, 0, 'lightgray'), ('8', 2, 1, 'lightgray'), ('9', 2, 2, 'lightgray'), ('/', 2, 3, 'orange'),
            ('4', 3, 0, 'lightgray'), ('5', 3, 1, 'lightgray'), ('6', 3, 2, 'lightgray'), ('*', 3, 3, 'orange'),
            ('1', 4, 0, 'lightgray'), ('2', 4, 1, 'lightgray'), ('3', 4, 2, 'lightgray'), ('-', 4, 3, 'orange'),
            ('0', 5, 0, 'lightgray'), ('.', 5, 1, 'lightgray'), ('=', 5, 2, 'green'), ('+', 5, 3, 'orange'),
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
                })
                gui.entry.delete(0, tk.END)
                gui.entry.insert(tk.END, str(result))
            except Exception as e:
                gui.entry.delete(0, tk.END)
                gui.entry.insert(tk.END, "Error")
        elif char == 'CA':
            gui.entry.delete(0, tk.END)
        elif char == 'C':
            current_text = gui.entry.get()
            if current_text:
                new_text = current_text[:-1]
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
