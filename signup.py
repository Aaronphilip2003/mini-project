from tkinter import * # helps to create GUI
import sqlite3 # database management system

conn=sqlite3.connect('people.db') # Making a database
cursor=conn.cursor() # Helps you navigate around the db file

cursor.execute("CREATE TABLE IF NOT EXISTS names(first_name text)") 

def insert():
    name=e.get() # It gets whatever is placed inside the entry box
    cursor.execute("INSERT INTO names VALUES (?)",(name,)) # adds data to names table
    conn.commit() # saves changes to the database
    e.delete(0,END) # clearing the entry box for future entries

root=Tk() # GUI through tkinter
root.geometry("500x300")
root.title("Add Name to Database")


lbl_main=Label(root,text="Database Entry")
lbl_main.place(x=180,y=50)

first_name=Label(root,text="First Name : ")
first_name.place(x=50,y=100)

e=Entry(root, borderwidth=5, width=50)
e.place(x=120,y=100)

button_insert=Button(root,text="INSERT",command=insert)
button_insert.place(x=200,y=200)
root.mainloop() # Keeps gui on screen till we click the cross button
conn.close() # Close connection to db to prevent ppl from changing values


# Label - Lets you place text on the GUI
# Button - YOU need to add functionality
# Entry box - A box where the user can enter using the keyboard