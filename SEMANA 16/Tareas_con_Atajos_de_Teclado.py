import tkinter as tk
from tkinter import messagebox

# Funciones para manejar las tareas
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        entry.focus()  # Regresar el foco al campo de entrada
        print(f"Tarea añadida: {task}")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

def complete_task(event=None):
    try:
        selected_task = listbox.curselection()
        if selected_task:
            task = listbox.get(selected_task)
            listbox.delete(selected_task)
            listbox.insert(selected_task, task + " - Completada")
            print(f"Tarea completada: {task}")
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea.")
    except Exception as e:
        print(f"Error: {e}")

def delete_task(event=None):
    try:
        selected_task = listbox.curselection()
        if selected_task:
            task = listbox.get(selected_task)
            listbox.delete(selected_task)
            print(f"Tarea eliminada: {task}")
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea.")
    except Exception as e:
        print(f"Error: {e}")

def close_app(event=None):
    root.quit()

# Función para detectar y mostrar las teclas presionadas
def detect_key(event):
    print(f"Tecla presionada: {event.keysym}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("450x500")
root.config(bg="#f0f0f0")  # Fondo gris claro para la ventana

# Campo de entrada
entry = tk.Entry(root, width=40, font=("Arial", 14), bd=2, relief="sunken")
entry.pack(pady=20)

# Botones con colores
button_add = tk.Button(root, text="Añadir Tarea", width=20, font=("Arial", 12), bg="#4CAF50", fg="white", command=add_task)
button_add.pack(pady=5)

button_complete = tk.Button(root, text="Marcar como Completada", width=20, font=("Arial", 12), bg="#2196F3", fg="white", command=complete_task)
button_complete.pack(pady=5)

button_delete = tk.Button(root, text="Eliminar Tarea", width=20, font=("Arial", 12), bg="#f44336", fg="white", command=delete_task)
button_delete.pack(pady=5)

# Lista de tareas con color de fondo y bordes
listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12), bd=2, relief="sunken", selectmode=tk.SINGLE, bg="#e0f7fa")
listbox.pack(pady=10)

# Asignación de atajos de teclado
root.bind('<Return>', lambda event: add_task())
root.bind('<c>', complete_task)
root.bind('<BackSpace>', delete_task)
root.bind('<Escape>', close_app)

# Detectar teclas presionadas en cualquier parte de la ventana
root.bind('<Key>', detect_key)

# Iniciar la aplicación
root.mainloop()

