import tkinter as tk
from tkinter import font as tkfont

# Function to update the input field
def press(key):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + key)

# Function to calculate the expression
def equalpress():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.configure(bg='#f0f0f0')

# Custom font
custom_font = tkfont.Font(family="Arial", size=18, weight="bold")

# Entry field
entry = tk.Entry(root, justify='right', font=custom_font, bd=5, insertwidth=4, width=15, bg='#ffffff', fg='#333333')
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Buttons
buttons = ['C', '(', ')', '/',
           '7', '8', '9', '*',
           '4', '5', '6', '+',
           '1', '2', '3', '-',
           '.', '0', '%', '=']

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: press(x) if x not in ['=', 'C'] else equalpress() if x == '=' else clear()
    if button=='C':
        tk.Button(root, text=button, bg='#4CAF50', fg='#ffffff', padx=20, pady=10, bd=8, font=custom_font, command=action).grid(row=row_val, column=col_val)
        col_val += 1
    elif button=='=':
        tk.Button(root, text=button, bg='#FF9800', fg='#ffffff', padx=20, pady=10, bd=8, font=custom_font, command=action).grid(row=row_val, column=col_val)
        col_val += 1
    else:
        tk.Button(root, text=button, bg='#e0e0e0', fg='#333333', padx=20, pady=10, bd=8, font=custom_font, command=action).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

# Run the application
root.mainloop()
