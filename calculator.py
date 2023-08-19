import tkinter as tk

class SimpleCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.entry = tk.Entry(root, font=("Helvetica", 16))
        self.entry.grid(row=0, column=0, columnspan=4)
        
        self.create_buttons()
    
    def create_buttons(self):
        """
                Create buttons
        """
        buttons = [     
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]
        
        for button_text, row, column in buttons:
            button = tk.Button(self.root, text=button_text, font=("Helvetica", 16), command=lambda text=button_text: self.on_button_click(text))
            button.grid(row=row, column=column, padx=10, pady=10)
    
    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, button_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculatorApp(root)
    root.mainloop()
