import tkinter as tk

def button_click(symbol):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + symbol)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("My Calculator")

# Create display
display = tk.Entry(root, width=50, borderwidth=7)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create buttons
for symbol, row, column in buttons:
    button = tk.Button(root, text=symbol, padx=20, pady=20, command=lambda sym=symbol: button_click(sym))
    button.grid(row=row, column=column, padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text="Clear", padx=20, pady=20, command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", padx=20, pady=20, command=calculate)
calculate_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()

