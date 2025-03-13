import tkinter as tk
from tkinter import messagebox

# Aplicación básica de gestión de productos
# Esta aplicación permite a los usuarios agregar productos con su precio a una lista y limpiarla cuando sea necesario.

def agregar_producto():
    producto = entrada_nombre.get()
    precio = entrada_precio.get()
    if producto and precio:
        try:
            precio = float(precio)
            lista.insert(tk.END, f"{producto} - ${precio:.2f}")
            entrada_nombre.delete(0, tk.END)
            entrada_precio.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un precio válido.")
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, ingrese un nombre y un precio.")

def limpiar_lista():
    lista.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Productos")  # Título más detallado
root.geometry("450x350")

# Crear y colocar widgets
etiqueta_nombre = tk.Label(root, text="Nombre del Producto:")
etiqueta_nombre.pack(pady=5)

entrada_nombre = tk.Entry(root, width=40)
entrada_nombre.pack(pady=5)

etiqueta_precio = tk.Label(root, text="Precio:")
etiqueta_precio.pack(pady=5)

entrada_precio = tk.Entry(root, width=40)
entrada_precio.pack(pady=5)

boton_agregar = tk.Button(root, text="Agregar Producto", command=agregar_producto)
boton_agregar.pack(pady=5)

lista = tk.Listbox(root, width=50, height=10)
lista.pack(pady=5)

boton_limpiar = tk.Button(root, text="Limpiar Lista", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
