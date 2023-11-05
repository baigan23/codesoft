import random
import string
from tkinter import *

def generate_password():
    length = int(var.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    label.config(text=password)

root = Tk()
root.title("Password Generator")

var = IntVar()
label = Label(root, text="", font=("Helvetica", 20))
entry = Spinbox(root, from_=8, to=100, textvariable=var, font=("Helvetica", 20))
button = Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 20))

label.pack(pady=20)
entry.pack(pady=20)
button.pack(pady=20)

root.mainloop()