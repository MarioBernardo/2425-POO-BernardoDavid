import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def agregar_evento():
    fecha = date_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()
    if fecha and hora and descripcion:
        eventos_tree.insert("", "end", values=(fecha, hora, descripcion))
        date_entry.set_date("")
        hora_entry.delete(0, tk.END)
        descripcion_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.")

def eliminar_evento():
    seleccionado = eventos_tree.selection()
    if seleccionado:
        for item in seleccionado:
            eventos_tree.delete(item)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Frame de entrada de datos
input_frame = ttk.Frame(root, padding="10")
input_frame.pack(fill="x")

ttk.Label(input_frame, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
date_entry = DateEntry(input_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
hora_entry = ttk.Entry(input_frame)
hora_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
descripcion_entry = ttk.Entry(input_frame)
descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

# Botón para agregar evento
agregar_btn = ttk.Button(input_frame, text="Agregar Evento", command=agregar_evento)
agregar_btn.grid(row=3, columnspan=2, pady=10)

# Frame para la lista de eventos
eventos_frame = ttk.Frame(root, padding="10")
eventos_frame.pack(fill="both", expand=True)

eventos_tree = ttk.Treeview(eventos_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
eventos_tree.heading("Fecha", text="Fecha")
eventos_tree.heading("Hora", text="Hora")
eventos_tree.heading("Descripción", text="Descripción")
eventos_tree.pack(fill="both", expand=True)

# Botón para eliminar evento
eliminar_btn = ttk.Button(root, text="Eliminar Evento Seleccionado", command=eliminar_evento)
eliminar_btn.pack(pady=5)

# Botón para salir
salir_btn = ttk.Button(root, text="Salir", command=root.quit)
salir_btn.pack(pady=5)

root.mainloop()
