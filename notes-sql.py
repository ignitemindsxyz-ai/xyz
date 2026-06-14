import mysql.connector
import tkinter as tk
from tkinter import messagebox,ttk

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "3rd_database"
)

cursor = conn.cursor()


def add_note(): 
    title = title_entry.get()
    body = body_text.get("1.0", tk.END).strip()
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

def search_category():
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

    note = cursor.fetchone()

    id_entry.delete(0, tk.END)
    id_entry.insert(0, note[0])

    title_entry.delete(0, tk.END)
    title_entry.insert(0, note[1])

    body_text.delete(0, tk.END)
    body_text.insert(0, note[2])

    category_entry.delete(0, tk.END)
    category_entry.insert(0, note[3])

def clear_fields():
    id_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    body_text.delete("1.0", tk.END)
    category_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Notes App")
root.geometry("800x600")

tk.Label(root, text="ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Title").pack()
title_entry = tk.Entry(root, width=50)
title_entry.pack()

tk.Label(root, text="Body").pack()
body_text = tk.Text(root, height=8, width=60)
body_text.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root, width=40)
category_entry.pack()

tk.Button(root, text="Add Note", command=add_note).pack(pady=5)
tk.Button(root, text="Update Note", command=update_note).pack(pady=5)
tk.Button(root, text="Delete Note", command=delete_note).pack(pady=5)
tk.Button(root, text="Search Category", command=search_category).pack(pady=5)
tk.Button(root, text="Refresh", command=view_note).pack(pady=5)

notes_list = ttk.Treeview(
    root,
    columns=("ID", "Title", "Body", "Category"),
    show="headings"
)

notes_list.heading("ID", text="ID")
notes_list.heading("Title", text="Title")
notes_list.heading("Body", text="Body")
notes_list.heading("Category", text="Category")

notes_list.pack(fill=tk.BOTH, expand=True)

notes_list.bind("<<TreeviewSelect>>", select_note)

view_note()

root.mainloop()

cursor.close()
conn.close()