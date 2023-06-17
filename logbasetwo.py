import tkinter as tk
from tkinter import ttk 

class Application(tk.Tk):
    """Application Root Window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("LogBaseTwo")
        self.resizable(width=False, height=False)
        self.geometry("600x300")
        self.logbasetwo = LogCalculator(self, padding = "8 8 12 12").grid(row = 0)

class LogCalculator(ttk.Frame):
    """Calculates Log Base Two"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.copyIcon = tk.PhotoImage(file=r"./assets/copy.png")
        self.copyIcon.configure(height=16, width=16)
        self.input = tk.StringVar()
        ttk.Label(self, text="lg", font=("Segoe UI", 16) ).grid(row=0, column=0)
        self.entry_form = ttk.Entry(self, textvariable=self.input, font=("Segoe UI", 16)).grid(row=0, column=1)
        ttk.Button(self, text="=", command=self.calculate).grid(row=0, column=2)
        self.output_text = tk.StringVar()
        self.output_text.set("Enter a value")
        ttk.Label(self, textvariable=self.output_text, font=("Segoe UI", 16)).grid(row=0, column=3)
        self.copy_status = tk.StringVar()
        self.copy_status.set("Copy")
    def calculate(self):
        import math
        try:
            self.output_text.set(math.log2(float(self.input.get())))
            self.copy_status.set("Copy")
            ttk.Button(self, textvariable=self.copy_status, command=self.copy).grid(row=0, column=4)
        except ValueError:
            self.output_text.set("Bad input")
    def copy(self):
        self.clipboard_append(self.output_text.get())
        self.copy_status.set("Copied")



if __name__ == "__main__":
    app = Application()
    app.mainloop()
