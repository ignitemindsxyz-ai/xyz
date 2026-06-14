import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk

conn   = mysql.connector.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='school_db')

cursor = conn.cursor()

def add_student():
    name = name_entry.get()


root = tk.Tk()
root.title("Student Information Manager")
root.geometry("400x400")
root.configure(bg="#302B2B")

tk.Button(root, text="Add Student", width=12, height=2, bg="#093B41", fg="White", font=("Sans", 12)).place(x=15, y=10)
tk.Button(root, text="Delete Student", width=12, height=2, bg="#093B41", fg="White", font=("Sans", 12)).place(x=15, y=70)
tk.Button(root, text="Update Student", width=12, height=2, bg="#093B41", fg="White", font=("Sans", 12)).place(x=15, y=130)
tk.Button(root, text="View Students", width=12, height=2, bg="#093B41", fg="White", font=("Sans", 12)).place(x=15, y=190)
tk.Button(root, text="Add Course", width=12, height=2, bg="#093B41", fg="White", font=("Sans", 12)).place(x=15, y=250)



root.mainloop()

cursor.close()
conn.close()