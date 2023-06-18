import tkinter as tk
from tkinter import ttk 


# fonts
title_font = ("TkDefaultFont", 24, "bold")
sub_title_font = ("TkDefaultFont", 16)
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
        unitConversion = ttk.Frame(notebook)
        notebook.add(log2frame, text="Log Base Two")
        notebook.add(baseConversion, text="Base Conversion")
        notebook.add(unitConversion, text="Unit Conversion")
        LogCalculator(log2frame).grid(row = 0, padx=16, pady=24)
        BaseConversion(baseConversion).grid(row=0, padx=16, pady=24)


class LogCalculator(tk.Frame):
    """Calculates Log Base Two"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Label(self, text="log\u2082", font=title_font).grid(row=0, column=0, sticky="w")
        self.input = tk.StringVar(self)
        self.entry = Entry(self, textvariable=self.input, font=input_font)
        self.entry.grid(row=1, column=0, pady=24, sticky="w")
        self.output_text = tk.StringVar(self)
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
            ttk.Label(self, text="Previous Results", font=("TkDefaultFont", 16, "bold")).grid(row=4, column=0, pady=24, sticky="w")
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

class BaseConversion(tk.Frame):
    """Base Conversion Calculator"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.option_var = tk.StringVar(self)
        self.option_var.set("Hexadecimal")
        self.options = ("Hexadecimal", 'Binary', "Decimal", "Octal", "Sexagesimal")
        ttk.OptionMenu(self, self.option_var, self.options[0], *self.options, command=self.option_changed).grid(row=0, column=0)
        self.input = tk.StringVar(self)
        self.entry = Entry(self, textvariable=self.input, font=input_font)
        self.entry.grid(row=0, column=1)

        # output
        self.out_frame = tk.Frame(self)
        self.out_frame.grid(row=1)
        ttk.Label(self.out_frame, text="Binary", font=sub_title_font).grid(row=0, column=0, sticky="w")
        binary_out = tk.StringVar(self.out_frame)
        binary_out.set("100100101")
        ttk.Label(self.out_frame, textvariable=binary_out, font=()).grid(row=0, column=1, sticky="e")

    def option_changed(self, *args):
        print(self.option_var.get())
if __name__ == "__main__":
    app = Application()
    app.mainloop()
