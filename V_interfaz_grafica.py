import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Jefe(Empleado):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)

class Area:
    def __init__(self, nombre):
        self.nombre = nombre

class GestionEmpleadosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Empleados")
        self.root.geometry("600x400")

        # Etiqueta de título
        self.title_label = tk.Label(self.root, text="Bienvenido al Sistema de Gestión de Empleados", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Botones
        self.btn_empleado = tk.Button(self.root, text="Ingresar datos de un empleado", command=self.ingresar_datos_empleado)
        self.btn_empleado.pack(pady=5)

        self.btn_jefe = tk.Button(self.root, text="Ingresar datos de un jefe", command=self.ingresar_datos_jefe)
        self.btn_jefe.pack(pady=5)

        self.btn_area = tk.Button(self.root, text="Ingresar datos de un área", command=self.ingresar_datos_area)
        self.btn_area.pack(pady=5)

    def ingresar_datos_empleado(self):
        # Ventana para ingresar datos de empleado
        self.empleado_window = tk.Toplevel()
        self.empleado_window.title("Ingresar datos de un empleado")
        self.empleado_window.geometry("400x300")

        # Campos de entrada
        self.nombre_label = tk.Label(self.empleado_window, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self.empleado_window)
        self.nombre_entry.pack()

        self.apellido_label = tk.Label(self.empleado_window, text="Apellido:")
        self.apellido_label.pack()
        self.apellido_entry = tk.Entry(self.empleado_window)
        self.apellido_entry.pack()

        # Botón para guardar datos
        self.guardar_btn = tk.Button(self.empleado_window, text="Guardar", command=self.guardar_empleado)
        self.guardar_btn.pack()

    def guardar_empleado(self):
        # Aquí puedes obtener los datos ingresados por el usuario
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()

        # Aquí puedes hacer lo que desees con los datos, como crear un nuevo objeto Empleado
        # Por ejemplo:
        nuevo_empleado = Empleado(nombre, apellido)
        # Luego, puedes agregar el nuevo empleado a una lista, guardar en un archivo, etc.

        # Mostrar mensaje de confirmación
        messagebox.showinfo("Mensaje", "Empleado guardado exitosamente.")

    def ingresar_datos_jefe(self):
        # Ventana para ingresar datos de jefe
        self.jefe_window = tk.Toplevel()
        self.jefe_window.title("Ingresar datos de un jefe")
        self.jefe_window.geometry("400x300")

        # Campos de entrada para jefe
        self.nombre_label = tk.Label(self.jefe_window, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self.jefe_window)
        self.nombre_entry.pack()

        # Botón para guardar datos
        self.guardar_btn = tk.Button(self.jefe_window, text="Guardar", command=self.guardar_jefe)
        self.guardar_btn.pack()

    def guardar_jefe(self):
        # Aquí puedes obtener los datos ingresados por el usuario para el jefe
        nombre = self.nombre_entry.get()

        # Aquí puedes hacer lo que desees con los datos del jefe
        # Por ejemplo:
        nuevo_jefe = Jefe(nombre, "")
        # Luego, puedes agregar el nuevo jefe a una lista, guardar en un archivo, etc.

        # Mostrar mensaje de confirmación
        messagebox.showinfo("Mensaje", "Jefe guardado exitosamente.")

    def ingresar_datos_area(self):
        # Ventana para ingresar datos de área
        self.area_window = tk.Toplevel()
        self.area_window.title("Ingresar datos de un área")
        self.area_window.geometry("400x300")

        # Campos de entrada para área
        self.nombre_label = tk.Label(self.area_window, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self.area_window)
        self.nombre_entry.pack()

        # Botón para guardar datos
        self.guardar_btn = tk.Button(self.area_window, text="Guardar", command=self.guardar_area)
        self.guardar_btn.pack()

    def guardar_area(self):
        # Aquí puedes obtener los datos ingresados por el usuario para el área
        nombre = self.nombre_entry.get()

        # Aquí puedes hacer lo que desees con los datos del área
        # Por ejemplo:
        nueva_area = Area(nombre)
        # Luego, puedes agregar la nueva área a una lista, guardar en un archivo, etc.

        # Mostrar mensaje de confirmación
        messagebox.showinfo("Mensaje", "Área guardada exitosamente.")

root = tk.Tk()
app = GestionEmpleadosApp(root)
root.mainloop()
