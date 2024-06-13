import tkinter as tk 
from function import add, subtract, multiply, divide  

class Calculator:
    def __init__(gui, root):
        gui.root = root
        gui.root.title("Grabe Ka Basic nga Calculator")
        
        gui.create_ui()

    def create_ui(gui):
        gui.entry = tk.Entry(gui.root, font=('Arial', 24), bd=8, insertwidth=1)
        gui.entry.grid(row=0, column=0, columnspan=4) 

      
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 3), ('=', 4, 2),
            ('CA',5, 0), ('secret',5, 1), ('',5, 2),('',5, 3),
        ]

        for (text, row, col) in buttons:
            gui.create_button(text, row, col)

        gui.root.grid_rowconfigure(5, weight=1)
        gui.root.grid_columnconfigure(4, weight=1)
        
    def create_button(gui, text, row, col):
        button = tk.Button(gui.root, text=text, padx=20, pady=20, font=('Arial', 18),
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
                    'divide': divide
                })
             
                gui.entry.delete(0, tk.END)
                gui.entry.insert(tk.END, str(result))
            except Exception as e:
  
                gui.entry.delete(0, tk.END)
                gui.entry.insert(tk.END, "Error")
                
        elif char == 'CA':
        
            gui.entry.delete(0, tk.END)
        elif char == 'secret':
            gui.entry.insert(tk.END, "Regards ko sa inyong Idol HAHAHAH")
            pass
        else:
        
            current_text = gui.entry.get()
            new_text = current_text + str(char)
            gui.entry.delete(0, tk.END)
            gui.entry.insert(tk.END, new_text)
            

if __name__ == "__main__":
    root = tk.Tk()  
    calculator = Calculator(root)  
    root.mainloop() 


