from tkinter import simpledialog
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *

def eingabe():
    user = name.get()
    with open("names.csv", "r") as file:  
         for line in file:
            split = line.strip().split(",") 
            if user == split[1]: 
                print(split[1], split[2], split[3], split[4], split[5])
                break

root = tk.Tk()
root.geometry("800x500")
root.title("NameStats")

label = tk.Label(root, text="NameStats", font=('Arial', 18))
label.pack(padx=20, pady=20)

name = tk.Entry(root)
name.pack()
name.focus()

# You had "Button" instead of "tk.Button" for creating the button widget.
b = tk.Button(root, text="Submit", command=eingabe)
b.pack()

root.mainloop()


"""
with open("../names.csv", "r") as file:   
    
    
    for line in file:
        split = line.strip().split(",") 
        if name == split[1]: 
            print(split[1], split[2], split[3], split[4], split[5])
            break

"""


