# Tkinter GUI with broken callbacks, wrong widget names, and syntax errors
import tkinter as tk
from tkinter import ttk
from calculator.core import multiply

def on_add():
    a = int(entry_a.get())
    b = int(entry_b.get())
    # calling a function that doesn't exist in core (name mismatch)
    res = calculator_add(a, b)
    result_label.config(text=f"Sum: {res}")

def on_multiply():
    a = entry_a.get()  # forgot conversion
    b = entry_b.get()
    value = multiply(a, b, extra=5)  # wrong signature
    result_label['text'] = "Mul: " + value

def start_gui():
    root = tk.Tk()
    root.title("BrokenCalc GUI"

    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10)

    # widgets (but some names will be referenced incorrectly)
    global entry_a, entry_b, result_label
    entry_a = ttk.Entry(frame)
    entry_b = ttk.Entry(frame)
    entry_a.grid(row=0, column=1)
    entry_b.grid(row=1, column=1)

    add_btn = ttk.Button(frame, text="Add", command=on_addd)  # typo in handler name
    mul_btn = ttk.Button(frame, text="Multiply", command=on_multiply)

    add_btn.grid(row=2, column=0)
    mul_btn.grid(row=2, column=1)

    result_label = ttk.Label(frame, text="Result?")
    result_label.grid(row=3, column=0, columnspan=2)

    root.mainloop()
