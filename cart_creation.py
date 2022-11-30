from tkinter import *
import sqlite3
import os


conn=sqlite3.connect("people.db") # connect to people's database
cursor=conn.cursor() # used to navigate inside a database

cursor.execute("SELECT * FROM names")
table=cursor.fetchall() # aaron arya aryan

list_names=[] # empty list to store the names of the members of the people database

for row in table:
    list_names.append(row[0]) # list_names.append(row) ["aaron"],["arya"],["aryan"],["allan"]

print(list_names) # print the list

conn.close() # close the connection

for i in list_names: # i="aaron"
    conn=sqlite3.connect(os.path.join('./databases',f"{i}.db"))
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS CART(item_name)")
    conn.close()
