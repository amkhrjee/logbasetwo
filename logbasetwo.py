import tkinter as tk
from tkinter import ttk 

class Application(tk.Tk):
    """Application Root Window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("LogBaseTwo")
        self.resizable(width=False, height=False)
        # self.geometry("400x350")
        notebook = ttk.Notebook(self)
        notebook.grid(row=0)
        log2frame = ttk.Frame(notebook)
        baseConversion = ttk.Frame(notebook)
        notebook.add(log2frame, text="Log Base Two")
        notebook.add(baseConversion, text="Base Conversion")
        LogCalculator(log2frame).grid(row = 0, padx=24, pady=24)


class LogCalculator(tk.Frame):
    """Calculates Log Base Two"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.copyIcon = tk.PhotoImage(file=r"./assets/copy.png")
        # self.copyIcon.configure(height=16, width=16)
        self.input = tk.StringVar()
        ttk.Label(self, text="lg", font=("Segoe UI", 16)).grid(row=0, column=0, sticky=(tk.E))
        Entry(self,  textvariable=self.input, font=("Segoe UI", 16)).grid(row=0, column=1)
        ttk.Button(self, text="=", command=self.calculate).grid(row=1, column=0)
        self.output_text = tk.StringVar()
        self.output_text.set("Enter a value")
        ttk.Label(self, textvariable=self.output_text, font=("Segoe UI", 16)).grid(row=1, column=1)
        self.copy_status = tk.StringVar()
        self.copy_status.set("Copy")
    def calculate(self):
        import math
        try:
            self.output_text.set(math.log2(float(self.input.get())))
            self.copy_status.set("Copy")
            ttk.Button(self, textvariable=self.copy_status, command=self.copy).grid(row=2, column=1)
        except ValueError:
            self.output_text.set("Bad input")
    def copy(self):
        self.clipboard_clear()
        self.clipboard_append(self.output_text.get())
        self.copy_status.set("Copied")

class Entry(ttk.Entry):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.focus()
        


if __name__ == "__main__":
    app = Application()
    app.mainloop()
