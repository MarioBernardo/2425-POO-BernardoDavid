import tkinter as tk
from tkinter import messagebox
from tkinter import font

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía")

def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, f"✔ {task}")
        task_listbox.itemconfig(selected_task_index, {'fg': 'green'})
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada")

def mark_pending():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        if task.startswith("✔ "):
            task = task[2:]  # Eliminar la marca de completado
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, task)
        task_listbox.itemconfig(selected_task_index, {'fg': 'black'})
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como pendiente")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

def on_enter_pressed(event):
    add_task()

def double_click_complete(event):
    mark_completed()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("450x450")
root.configure(bg="#f0f0f0")

# Fuente personalizada
task_font = font.Font(family="Arial", size=12)

# Entrada de tarea
task_entry = tk.Entry(root, width=40, font=task_font)
task_entry.pack(pady=10)
task_entry.bind("<Return>", on_enter_pressed)

# Botones
button_frame = tk.Frame(root)
button_frame.pack()

add_button = tk.Button(button_frame, text="Añadir Tarea", command=add_task, bg="#4caf50", fg="white", padx=10, pady=5)
add_button.grid(row=0, column=0, padx=5, pady=5)

complete_button = tk.Button(button_frame, text="Marcar como Completada", command=mark_completed, bg="#2196f3", fg="white", padx=10, pady=5)
complete_button.grid(row=0, column=1, padx=5, pady=5)

pending_button = tk.Button(button_frame, text="Marcar como Pendiente", command=mark_pending, bg="#ff9800", fg="white", padx=10, pady=5)
pending_button.grid(row=0, column=2, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=delete_task, bg="#f44336", fg="white", padx=10, pady=5)
delete_button.grid(row=0, column=3, padx=5, pady=5)

# Lista de tareas
task_listbox = tk.Listbox(root, width=50, height=10, font=task_font, selectbackground="#d3d3d3")
task_listbox.pack(pady=10)
task_listbox.bind("<Double-Button-1>", double_click_complete)

# Ejecutar la aplicación
root.mainloop()
