import tkinter as tk
from tkinter.colorchooser import *
import mysql.connector
cdbs ="DATABASE successfully created !"
cdbf ="Something else went wrong !"
dbae ="Database already exists"
mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = ""
)
exe=mydb.cursor()
def cdb(dbname):
    exe = mydb.cursor()
    cdb ="CREATE DATABASE "
    sql = cdb+dbname
    try:
        exe.execute(sql)
        mydb.commit()
        return cdbs
    except mysql.connector.errors.DatabaseError:
        return dbae
    except:
        return cdbf
def create():
    result=cdb(str(entryText.get()))
    info.config(text=result)
mw = tk.Tk()
mw.title('Create Database')
mw.geometry("400x400") 
mw.resizable()
entryText = tk.Entry(text=1, bg='white', fg='black')
entryText.place(x = 100, y = 50, width=200, height=50)
btn = tk.Button(text='Create', command=create)
btn.place(x = 100, y = 150, width=200, height=50)
info = tk.Label(text='result', bg='white', fg='black')
info.place(x = 50, y = 250, width=300, height=100)
mw.mainloop()