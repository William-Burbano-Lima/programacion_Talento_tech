import csv

# Definimos la clase Empleado
class Empleado:
    def __init__(self, nombre, apellido, edad, salario, dni, fecha_vinculacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario
        self.dni = dni
        self.fecha_vinculacion = fecha_vinculacion

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Edad: {self.edad}, Salario: {self.salario}, DNI: {self.dni}, Fecha de Vinculación: {self.fecha_vinculacion}"

# Definimos la clase Jefe, que hereda de Empleado
class Jefe(Empleado):
    def __init__(self, nombre, apellido, edad, salario, dni, fecha_vinculacion):
        super().__init__(nombre, apellido, edad, salario, dni, fecha_vinculacion)
        self.empleados_a_cargo = []

    def agregar_empleado(self, empleado):
        self.empleados_a_cargo.append(empleado)

    def listar_empleados_a_cargo(self):
        return [empleado.obtener_nombre_completo() for empleado in self.empleados_a_cargo]

    def __str__(self):
        return f"{super().__str__()}, Empleados a Cargo: {', '.join(self.listar_empleados_a_cargo())}"

# Definimos la clase Área
class Area:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def listar_empleados(self):
        return [empleado.obtener_nombre_completo() for empleado in self.empleados]

    def __str__(self):
        return f"Área: {self.nombre}, Descripción: {self.descripcion}, Empleados: {', '.join(self.listar_empleados())}"

# Definimos la clase SistemaGestionEmpleados para gestionar todos los empleados, jefes y áreas
class SistemaGestionEmpleados:
    def __init__(self):
        self.empleados = []
        self.jefes = []
        self.areas = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_jefe(self, jefe):
        self.jefes.append(jefe)

    def agregar_area(self, area):
        self.areas.append(area)

    def guardar_datos(self, archivo_empleados, archivo_jefes, archivo_areas):
        with open(archivo_empleados, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Nombre', 'Apellido', 'Edad', 'Salario', 'DNI', 'Fecha de Vinculación'])
            for empleado in self.empleados:
                writer.writerow([empleado.nombre, empleado.apellido, empleado.edad, empleado.salario, empleado.dni, empleado.fecha_vinculacion])
        
        with open(archivo_jefes, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Nombre', 'Apellido', 'Edad', 'Salario', 'DNI', 'Fecha de Vinculación', 'Empleados a Cargo'])
            for jefe in self.jefes:
                writer.writerow([jefe.nombre, jefe.apellido, jefe.edad, jefe.salario, jefe.dni, jefe.fecha_vinculacion, ', '.join(jefe.listar_empleados_a_cargo())])
        
        with open(archivo_areas, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Nombre Área', 'Descripción', 'Empleados'])
            for area in self.areas:
                writer.writerow([area.nombre, area.descripcion, ', '.join(area.listar_empleados())])

    def cargar_datos(self, archivo_empleados, archivo_jefes, archivo_areas):
        with open(archivo_empleados, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Saltar la primera fila que contiene los encabezados
            for row in reader:
                if len(row) < 6:
                    continue  # Ignorar filas incompletas
                empleado = Empleado(row[0], row[1], int(row[2]), float(row[3]), row[4], row[5])
                self.empleados.append(empleado)
        
        with open(archivo_jefes, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Saltar la primera fila que contiene los encabezados
            for row in reader:
                if len(row) < 6:
                    continue  # Ignorar filas incompletas
                jefe = Jefe(row[0], row[1], int(row[2]), float(row[3]), row[4], row[5])
                self.jefes.append(jefe)
                if len(row) > 6 and row[6]:
                    empleados_a_cargo = row[6].split(', ')
                    for emp_nombre in empleados_a_cargo:
                        for emp in self.empleados:
                            if emp.obtener_nombre_completo() == emp_nombre:
                                jefe.agregar_empleado(emp)

        with open(archivo_areas, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Saltar la primera fila que contiene los encabezados
            for row in reader:
                if len(row) < 3:
                    continue  # Ignorar filas incompletas
                area = Area(row[0], row[1])
                self.areas.append(area)
                if row[2]:
                    empleados_area = row[2].split(', ')
                    for emp_nombre in empleados_area:
                        for emp in self.empleados:
                            if emp.obtener_nombre_completo() == emp_nombre:
                                area.agregar_empleado(emp)
# hasta aqui va las funciones del taller
# Ejemplo de uso:
# Crear el sistema de gestión de empleados
sistema = SistemaGestionEmpleados()

# Crear empleados
empleado1 = Empleado("Juan", "Perez", 30, 30000, "12345678", "01/01/2020")
empleado2 = Empleado("Maria", "Gomez", 25, 25000, "87654321", "01/01/2021")
empleado3 = Empleado("Dolores", "Cabezas", 25, 25000, "65845887", "01/01/20")
empleado4 = Empleado("Dolores2", "Cabezas2", 27, 250000, "658458878", "01/01/20")

# Crear jefes
jefe1 = Jefe("Carlos", "Lopez", 40, 40000, "98765432", "01/01/2010")
jefe2 = Jefe("Ana", "Martinez", 35, 35000, "54321678", "01/01/2012")
jefe3 = Jefe("Ana2", "Martinez", 35, 35000, "54321678", "01/01/2012")
# Asignar empleados a jefes
jefe1.agregar_empleado(empleado1)
jefe2.agregar_empleado(empleado2)
jefe3.agregar_empleado(empleado3)

# Crear áreas
area1 = Area("Ventas", "Departamento encargado de las ventas")
area2 = Area("Contabilidad", "Departamento encargado de la contabilidad")
area3 = Area("Informatica", "Departamento de las TIC")

# Asignar empleados a áreas
area1.agregar_empleado(empleado1)
area2.agregar_empleado(empleado2)

# Agregar empleados, jefes y áreas al sistema
sistema.agregar_empleado(empleado1)
sistema.agregar_empleado(empleado2)
sistema.agregar_jefe(jefe1)
sistema.agregar_jefe(jefe2)
sistema.agregar_area(area1)
sistema.agregar_area(area2)

# Guardar datos en archivos CSV
sistema.guardar_datos("empleados.csv", "jefes.csv", "areas.csv")

# Crear una nueva instancia del sistema para cargar los datos
sistema_cargado = SistemaGestionEmpleados()
sistema_cargado.cargar_datos("empleados.csv", "jefes.csv", "areas.csv")

# Mostrar los empleados, jefes y áreas cargados
print("Empleados:")
for empleado in sistema_cargado.empleados:
    print(empleado)

print("\nJefes:")
for jefe in sistema_cargado.jefes:
    print(jefe)

print("\nÁreas:")
for area in sistema_cargado.areas:
    print(area)
