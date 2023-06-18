import tkinter as tk
from tkinter import ttk 


# fonts
title_font = ("TkDefaultFont", 24, "bold")
input_font = ("TkDefaultFont", 24)

class Application(tk.Tk):
    """Application Root Window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("LogBaseTwo")
        self.resizable(width=False, height=False)
        # self.geometry("400x350")
        # menu bar
        self.option_add('*tearOff', tk.FALSE)
        menubar = tk.Menu(self)
        menu_file = tk.Menu(menubar)
        menu_pref = tk.Menu(menubar)
        menu_about = tk.Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_pref, label='Prefernces')
        menubar.add_cascade(menu=menu_about, label='About')
        self.config(menu=menubar)
        # tabs
        notebook = ttk.Notebook(self)
        notebook.grid(row=0)
        log2frame = ttk.Frame(notebook, padding="24")
        baseConversion = ttk.Frame(notebook)
        notebook.add(log2frame, text="Log Base Two")
        notebook.add(baseConversion, text="Base Conversion")
        LogCalculator(log2frame).grid(row = 0, padx=16, pady=24)


class LogCalculator(tk.Frame):
    """Calculates Log Base Two"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Label(self, text="log\u2082", font=title_font).grid(row=0, column=0, sticky="w")
        self.input = tk.StringVar()
        self.entry = Entry(self, textvariable=self.input, font=input_font)
        self.entry.grid(row=1, column=0, pady=24, sticky="w")
        self.output_text = tk.StringVar()
        self.output_text.set("")
        ttk.Label(self, textvariable=self.output_text, font=("TkDefaultFont", 24)).grid(row=2, column=0, sticky="w")
        self.copy_status = tk.StringVar()
        self.copy_status.set("Copy to clipboard")
        self.entry.bind("<Return>", self.calculate)
        self.prev_results = {}
        self.rowcount = 0

    def calculate(self, *args):
        import math
        try:
            self.output_text.set(math.log2(float(self.input.get())))
            prev_result_str = f"log\u2082({self.input.get()}) = {self.output_text.get()}"
            self.copy_status.set("Copy to clipboard")
            ttk.Button(self, textvariable=self.copy_status, command=self.copy).grid(row=3, column=0, sticky="w")
            ttk.Label(self, text="Previous Results", font=("TkDefaultFont", 20, "bold")).grid(row=4, column=0, pady=24, sticky="w")
            ttk.Label(self, text=prev_result_str, font=("TkDefaultFont", 12)).grid(row=(5+self.rowcount), column=0, sticky="w")
            self.rowcount += 1
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
