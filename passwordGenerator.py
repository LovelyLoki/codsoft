import tkinter as tk
from tkinter import *
import random
import string

password = ""

def Generate_password():
    global password
    try:
        if entry_1.get() and entry_2.get():
            length = int(entry_2.get())
            l = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(l) for i in range(length))
            password1 = "The Password Generated is :  "+password
            label_3.config(text=password1, fg='red')
        elif entry_2.get():
            password = "Enter User Name !!"
            label_3.config(text=password, fg='red')
        else:
            password = "Enter Desired Length of Password !!"
            label_3.config(text=password, fg='red')            
    except ValueError:
        print("Please enter a valid integer for the password length.")
        
def Reset():
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    label_3.config(text="")
    label_4.config(text="")

def Accept():
    global password
    s = "Hello "+entry_1.get()+"! your Password is :  "+password
    label_4.config(text=s)

window = tk.Tk()
window.geometry('800x700')
window.configure(bg='lightblue')  # Changed background color

label_1 = tk.Label(window, text="PASSWORD GENERATOR", font=("Rockwell", 30, "bold"), fg="black", bg='lightblue')
label_1.place(x=200, y=10)

label_2 = tk.Label(window, text="Enter User Name: ", font=("rockwell", 20), fg="black", bg='lightblue')
label_2.place(x=50, y=100)

entry_1 = tk.Entry(window, font=('rockwell', 20))
entry_1.place(x=280, y=100)

label_2 = tk.Label(window, text="Enter desired length of the password: ", font=("rockwell", 20), bg='lightblue')
label_2.place(x=50, y=180)
    
entry_2 = tk.Entry(window, font=('rockwell', 20))
entry_2.place(x=520, y=180)

button_1 = tk.Button(window, text="GENERATE", font=('rockwell', 20, "bold"), bg='lightgreen', command=Generate_password) # Changed button color
button_1.place(x=100, y=250)

button_2 = tk.Button(window, text="ACCEPT", font=('rockwell', 20, "bold"), bg='lightcoral', command=Accept) # Changed button color
button_2.place(x=300, y=250)

button_3 = tk.Button(window, text=" RESET ", font=('rockwell', 20, "bold"), bg='lightyellow', command=Reset) # Changed button color
button_3.place(x=500, y=250)

label_3 = tk.Label(window, font=("rockwell", 20, "bold"), bg='lightblue')
label_3.place(x=50, y=350)

label_4 = tk.Label(window, font=("rockwell", 20, "bold"), bg='lightblue')
label_4.place(x=50, y=450)

window.mainloop()
