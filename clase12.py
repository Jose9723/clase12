import tkinter as tk
from tkinter import messagebox

class Inventario:   
    def __init__(self):
        self.ventana = tk.Tk()  
        self.ventana.title("Inventario")
        self.ventana.geometry("400x500")  
        self.ventana.configure(bg='aqua')

        frame_producto = tk.Frame(self.ventana, bg='lightblue')
        frame_producto.pack(pady=10)

        self.etiqueta_producto = tk.Label(self.ventana, text="Producto:", bg='aqua', fg='darkblue', font=('Helvetica', 20))
        self.etiqueta_producto.pack()

        self.entrada_producto = tk.Entry(self.ventana, bg="black", fg="aqua", font=('Helvetica', 20))
        self.entrada_producto.pack(pady=(0,20))

        self.etiqueta_cantidad = tk.Label(self.ventana, text="Cantidad:", bg='aqua', fg='darkblue', font=('Helvetica', 20))
        self.etiqueta_cantidad.pack()

        self.entrada_cantidad = tk.Entry(self.ventana, bg="black", fg="aqua", font=('Helvetica', 20))
        self.entrada_cantidad.pack(pady=(0,20))

        self.boton_comprar = tk.Button(self.ventana, text="Comprar", bg="darkblue", fg='aqua', font=('Helvetica', 15), command=self.comprar_producto)
        self.boton_comprar.pack(pady=10)

        self.boton_vender = tk.Button(self.ventana, text="Vender", bg="darkblue", fg='aqua', font=('Helvetica', 15), command=self.vender_producto)
        self.boton_vender.pack(pady=10)

        self.boton_visualizar = tk.Button(self.ventana, text="Visualizar Inventario", bg="darkblue", fg='aqua', font=('Helvetica', 15), command=self.visualizar_inventario)
        self.boton_visualizar.pack(pady=15)

        self.inventario = {}

    def comprar_producto(self):
        producto = self.entrada_producto.get()
        try:
            cantidad = int(self.entrada_cantidad.get())
            if cantidad > 0:
                if producto in self.inventario:
                    self.inventario[producto] += cantidad
                else:
                    self.inventario[producto] = cantidad

                self.guardar_inventario()
                self.entrada_producto.delete(0, tk.END)
                self.entrada_cantidad.delete(0, tk.END)
            else:
                messagebox.showwarning("Error", "La cantidad debe ser un número positivo")
        except ValueError:
            messagebox.showwarning("Error", "Ingrese una cantidad válida")

    def vender_producto(self):
        producto = self.entrada_producto.get()
        try:
            cantidad = int(self.entrada_cantidad.get())
            if cantidad > 0:
                if producto in self.inventario:
                    if self.inventario[producto] >= cantidad:
                        self.inventario[producto] -= cantidad
                        if self.inventario[producto] == 0:
                            del self.inventario[producto]
                        self.guardar_inventario()
                        self.entrada_producto.delete(0, tk.END)
                        self.entrada_cantidad.delete(0, tk.END)
                    else:
                        messagebox.showwarning("Error", "No hay suficiente cantidad para vender")
                else:
                    messagebox.showwarning("Error", "El producto no está en el inventario")
            else:
                messagebox.showwarning("Error", "La cantidad debe ser un número positivo")
        except ValueError:
            messagebox.showwarning("Error", "Ingrese una cantidad válida")

    def visualizar_inventario(self):
        inventario_str = "\n".join(f"{producto}: {cantidad}" for producto, cantidad in self.inventario.items())
        messagebox.showinfo("Inventario", inventario_str if inventario_str else "El inventario está vacío")

    def guardar_inventario(self):
        with open("inventario.txt", "w") as archivo:
            for producto, cantidad in self.inventario.items():
                archivo.write(f"{producto}:{cantidad}\n")

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = Inventario()
    app.run()
