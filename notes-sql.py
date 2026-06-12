import mysql.connector
import tkinter as tk
from tkinter import messagebox,ttk

root = tk.Tk()
root.title("Simple Notes")
root.geometry('500x600')
root.configure(bg="#252823")

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "3rd_database"
)

cursor = conn.cursor()


def add_note(): 
    title = title_entry.get()
    body = body_entry.get("1.0", tk.END).strip()
    category = category_entry.get()

    sql = "INSERT INTO note (title, body, category) VALUES (%s, %s, %s)"
    values = (title, body, category)
    cursor.execute(sql, values)
    conn.commit()

    messagebox.showinfo("Success", "Note added")
    clear_fields()
    view_note()

def view_note():
    notes_list.delete(*notes_list.get_children())

    cursor.execute(
        "SELECT id, title, body, category FROM note"
    )

    for row in cursor.fetchall():
        notes_list.insert("", tk.END, values=row)

def delete_note():
    note_id = id_entry.get()

    if not note_id:
        messagebox.showerror("Error", "Enter Note ID")
        return

    cursor.execute(
        "DELETE FROM note WHERE id=%s",
        (note_id,)
    )
    conn.commit()
    messagebox.showinfo("Note deleted")
    view_note()

def update_note():
    note_id = id_entry.get()

    cursor.execute(
        """
        UPDATE note
        SET title=%s, body=%s, category=%s
        WHERE id=%s
        """,
        (
            title_entry.get(),
            body_text.get("1.0", tk.END).strip(),
            category_entry.get(),
            note_id
        )
    )

    conn.commit()

    messagebox.showinfo("Note updated")
    view_note()

def search_note():
    category = category_entry.get()

    notes_list.delete(*notes_list.get_children())

    cursor.execute(
        """
        SELECT id, title, category
        FROM note
        WHERE category=%s
        """,
        (category,)
    )

    for row in cursor.fetchall():
        notes_list.insert("", tk.END, values=row)

def select_note(event):
    selected = notes_list.focus()

    if not selected:
        return
    
    values = notes_list.item(selected, "values")

    note_id = values[0]

    cursor.execute(
        "SELECT * FROM note WHERE id=%s"
        (note_id)
    )

    