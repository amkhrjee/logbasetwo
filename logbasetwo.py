# Author: Aniruddha Mukherjee
# Last edit: June 2023

import os
if os.name == 'nt':
    import ctypes
    # app icon
    myappid = 'amkhrjee.dataentryapp.csvfiles.0.0.1'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
import webbrowser
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox


basedir = os.path.dirname(__file__)

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
        if os.name == 'nt':
            self.iconbitmap(os.path.join(basedir, "favicon.ico"))
        # menu bar
        self.option_add('*tearOff', tk.FALSE)
        menubar = tk.Menu(self)
        menu_file = tk.Menu(menubar)
        menu_pref = tk.Menu(menubar)
        menu_about = tk.Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_about, label='About')
        # menubar.add_cascade(menu=menu_pref, label='Preferences')
        self.config(menu=menubar)

        # menu items
        # File Menu
        menu_file.add_command(label="New Window", command=self.new_window)
        menu_file.add_command(label="Enable Transparency", command=self.make_transparent)
        menu_file.add_command(label="Disable Transparency", command=self.undo_transparent)
        menu_file.add_command(label="Quit", command=self.quit_app)
        # Preferences
        # todo

        # About
        menu_about.add_command(label="License", command=self.view_license)
        menu_about.add_command(label="Report Bug", command=self.report_bug)
        menu_about.add_command(label="View source code", command=self.view_source)
        # tabs
        notebook = ttk.Notebook(self)
        notebook.grid(row=0)
        log2frame = ttk.Frame(notebook, padding="24")
        baseConversion = ttk.Frame(notebook)
        # unitConversion = ttk.Frame(notebook)
        notebook.add(log2frame, text="Log Base Two")
        notebook.add(baseConversion, text="Base Conversion")
        # notebook.add(unitConversion, text="Unit Conversion")
        LogCalculator(log2frame).grid(row = 0, padx=16, pady=24)
        BaseConversion(baseConversion).grid(row=0, padx=16, pady=24)
        # UnitConversion(unitConversion).grid(row=0, padx=16, pady=24)
    def new_window(self):
        another_app = Application()
        another_app.mainloop()

    def quit_app(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.destroy()

    def make_transparent(self):
            self.attributes("-alpha", 0.8)

    def undo_transparent(self):
            self.attributes("-alpha", 1.0)
    def view_license(self):
        webbrowser.open_new("https://github.com/amkhrjee/logbasetwo/blob/main/LICENSE")

    def report_bug(self):
        webbrowser.open_new("https://github.com/amkhrjee/logbasetwo/issues/new")

    def view_source(self):
        webbrowser.open_new("https://github.com/amkhrjee/logbasetwo")

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
        self.copy_status = tk.StringVar(self)
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
        self.options = ("Hexadecimal", "Binary", "Decimal", "Octal", "Sexagesimal")
        ttk.OptionMenu(self, self.option_var, self.options[0], *self.options).grid(row=0, column=0)
        self.input = tk.StringVar(self)
        self.entry = Entry(self, textvariable=self.input, font=input_font)
        self.entry.grid(row=0, column=1)
        self.entry.bind("<Return>", self.calculate)

        # output
        self.out_frame = tk.Frame(self)
        self.out_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=24)
        # allocate all the available space horizontally to column 1 inside self.out_frame
        self.out_frame.columnconfigure(1, weight=1)

        self.hex_out = tk.StringVar(self.out_frame)
        self.octal_out = tk.StringVar(self.out_frame)
        self.binary_out = tk.StringVar(self.out_frame)
        self.decimal_out = tk.StringVar(self.out_frame)
        self.sexagesimal_out = tk.StringVar(self.out_frame)

        self.error = ttk.Label(text="Bad Input", font=sub_title_font)
        
    def calculate(self, *args):
        base = {
            "Binary": 2,
            "Octal": 8,
            "Hexadecimal": 16,
            "Sexagesimal": 60
        }
        self.error.grid_forget()
        try:
            input_num = int(self.input.get())
            if self.option_var.get() != "Decimal":
                decimal = int(self.input.get(), base[self.option_var.get()])
            else:
                decimal = input_num
            octal = oct(decimal)
            hexnum = hex(decimal)
            binary = bin(decimal)
            sexagesimal_txt = self.decimal_to_sexagesimal(decimal)
            self.hex_out.set(str(hexnum))
            self.binary_out.set(str(binary))
            self.decimal_out.set(str(decimal))
            self.octal_out.set(str(octal))
            self.sexagesimal_out.set(sexagesimal_txt)
            
            # hex
            if self.option_var.get() != "Hexadecimal":
                ttk.Label(self.out_frame, text="Hexadecimal", font=sub_title_font).grid(row=0, column=0, sticky="w")
                ttk.Label(self.out_frame, textvariable=self.hex_out, font=sub_title_font).grid(row=0, column=1, sticky="e")
                ttk.Separator(self.out_frame, orient=tk.HORIZONTAL).grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)
         
            # binary
            if self.option_var.get() != "Binary":
                ttk.Label(self.out_frame, text="Binary", font=sub_title_font).grid(row=2, column=0, sticky="w")
                ttk.Label(self.out_frame, textvariable=self.binary_out, font=sub_title_font).grid(row=2, column=1, sticky="e")
                ttk.Separator(self.out_frame, orient=tk.HORIZONTAL).grid(row=3, column=0, columnspan=2, sticky="ew", pady=5)
            
            # decimal
            if self.option_var.get() != "Decimal":
                ttk.Label(self.out_frame, text="Decimal", font=sub_title_font).grid(row=4, column=0, sticky="w")
                ttk.Label(self.out_frame, textvariable=self.decimal_out, font=sub_title_font).grid(row=4, column=1, sticky="e")
                ttk.Separator(self.out_frame, orient=tk.HORIZONTAL).grid(row=5, column=0, columnspan=2, sticky="ew", pady=5)
            
            # Octal
            if self.option_var.get() != "Octal":
                ttk.Label(self.out_frame, text="Octal", font=sub_title_font).grid(row=6, column=0, sticky="w")
                ttk.Label(self.out_frame, textvariable=self.octal_out, font=sub_title_font).grid(row=6, column=1, sticky="e")
                ttk.Separator(self.out_frame, orient=tk.HORIZONTAL).grid(row=7, column=0, columnspan=2, sticky="ew", pady=5)

            # sexagesimal
            if self.option_var.get() != "Sexagesimal":
                ttk.Label(self.out_frame, text="Sexagesimal", font=sub_title_font).grid(row=8, column=0, sticky="w")
                ttk.Label(self.out_frame, textvariable=self.sexagesimal_out, font=sub_title_font).grid(row=8, column=1, sticky="e")
        except ValueError:
            self.error.grid(row=0)
        
    def decimal_to_sexagesimal(self, decimal_number):
        degrees = int(decimal_number)
        minutes = int((decimal_number - degrees) * 60)
        seconds = int(((decimal_number - degrees) * 60 - minutes) * 60)
        sexagesimal = f"{degrees}°{minutes}'{seconds}\""
        return sexagesimal


if __name__ == "__main__":
    app = Application()
    app.mainloop()
