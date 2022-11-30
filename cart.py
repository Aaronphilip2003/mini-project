import os
import sqlite3
from tkinter import *


dir_path = r"./databases"
res = []
flag = 0


for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)

name_input = input("Enter your name:") # Aaron
name_input = name_input + ".db" # Aaron.db
file = "./databases/" + name_input # ./databases/Aaron.db

for files in res:
    if files == name_input:
        flag = 1
        break

if flag == 1:
    print("Continue To Shop...")

    def add_db():
        equipment = clicked.get() # MACBOOK AIR
        label.config(text=equipment) # Display MACBOOK AIR
        conn = sqlite3.connect(file)# Connect to allan.db
        cursor = conn.cursor() # navigate inside allan.db
        cursor.execute("INSERT INTO CART VALUES (?)", (equipment,))
        conn.commit()
        conn.close()

    root = Tk()

    root.geometry("450x450")
    root.title("SELECT THE ITEMS THAT YOU WANT TO BUY:")
    # Dropdown menu options
    options = [
        "APPLE IPHONE 14 PRO",
        "SAMSUNG GALAXY M31",
        "MACBOOK AIR",
        "MACBOOK PRO",
        "AMAZON $100 GIFT CARD",
        "TENNIS RACKET",
        "FORMULA 1 STICKERS",
    ]

    clicked = StringVar()
    clicked.set("FORMULA 1 STICKERS")

    drop = OptionMenu(root, clicked, *options)
    drop.pack()

    # Create button, it will change label text
    button = Button(root, text="Add to Cart", command=add_db).pack()

    label = Label(root, text=" ")
    label.pack()

    root.mainloop()
else:
    print("Signup or enter correct username to continue...")