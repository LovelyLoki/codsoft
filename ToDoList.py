import tkinter as tk
from tkinter import simpledialog, messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

def edit_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        new_task = simpledialog.askstring("Edit task", "Edit your task:", initialvalue=task)
        if new_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, new_task)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to edit.")

window = tk.Tk()
window.title('TO-DO List')
window.geometry("700x300")
window.configure(bg='#F5F5F5')  # Light gray background

label_1 = tk.Label(window, text="Enter Task:", font=("Arial", 14), bg='#F5F5F5', fg='#333333')  # Light gray background, dark gray text
label_1.pack(pady=10)

entry = tk.Entry(window, width=50, font=("Arial", 12), bg='#FFFFFF', fg='#333333')  # White background, dark gray text
entry.pack(pady=10)

add_button = tk.Button(window, text="Add Task", width=20, command=add_task, bg='#4CAF50', fg='#FFFFFF', font=("Arial", 12))  # Green button, white text
add_button.pack(pady=5)

edit_button = tk.Button(window, text="Edit Task", width=20, command=edit_task, bg='#2196F3', fg='#FFFFFF', font=("Arial", 12))  # Blue button, white text
edit_button.pack(pady=5)

remove_button = tk.Button(window, text="Remove Task", width=20, command=remove_task, bg='#E53935', fg='#FFFFFF', font=("Arial", 12))  # Red button, white text
remove_button.pack(pady=5)

listbox = tk.Listbox(window, width=50, height=10, font=("Arial", 12), bg='#FFFFFF', fg='#333333')  # White background, dark gray text
listbox.pack(pady=10)

window.mainloop()
