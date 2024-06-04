import csv
import os

class Empleado:
    def __init__(self, nombre, apellido, edad, salario, dni, fecha_vinculacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario
        self.dni = dni
        self.fecha_vinculacion = fecha_vinculacion
        self.jefe = None
        self.area = None

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Edad: {self.edad}, Salario: {self.salario}, DNI: {self.dni}, Fecha de Vinculación: {self.fecha_vinculacion}"

class Jefe(Empleado):
    def __init__(self, nombre, apellido, edad, salario, dni, fecha_vinculacion):
        super().__init__(nombre, apellido, edad, salario, dni, fecha_vinculacion)
        self.empleados_a_cargo = []

    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado) and empleado not in self.empleados_a_cargo:
            self.empleados_a_cargo.append(empleado)
            empleado.jefe = self

    def listar_empleados_a_cargo(self):
        return [empleado.obtener_nombre_completo() for empleado in self.empleados_a_cargo]

    def __str__(self):
        return f"{super().__str__()}, Empleados a Cargo: {', '.join(self.listar_empleados_a_cargo())}"

class Area:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleados = []
        self.jefe = None

    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado) and empleado not in self.empleados:
            self.empleados.append(empleado)
            empleado.area = self

    def listar_empleados(self):
        return [empleado.obtener_nombre_completo() for empleado in self.empleados]

    def __str__(self):
        return f"Área: {self.nombre}, Descripción: {self.descripcion}, Empleados: {', '.join(self.listar_empleados())}"

class SistemaGestionEmpleados:
    def __init__(self):
        self.empleados = []
        self.jefes = []
        self.areas = []

    def agregar_empleado(self, empleado):
        if self.consultar_empleado_por_dni(empleado.dni) is None:
            self.empleados.append(empleado)
            print(f"Empleado {empleado.obtener_nombre_completo()} agregado.")
        else:
            print(f"Empleado con DNI {empleado.dni} ya está registrado.")

    def agregar_jefe(self, jefe):
        if self.consultar_jefe_por_dni(jefe.dni) is None:
            self.jefes.append(jefe)
            print(f"Jefe {jefe.obtener_nombre_completo()} agregado.")
        else:
            print(f"Jefe con DNI {jefe.dni} ya está registrado.")

    def agregar_area(self, area):
        if self.consultar_area_por_nombre(area.nombre) is None:
            self.areas.append(area)
            print(f"Área {area.nombre} agregada.")
        else:
            print(f"Área {area.nombre} ya está registrada.")

    def ingresar_datos_empleado(self):
        nombre = input("Ingrese el nombre del empleado: ")
        apellido = input("Ingrese el apellido del empleado: ")
        edad = int(input("Ingrese la edad del empleado: "))
        salario = float(input("Ingrese el salario del empleado: "))
        dni = input("Ingrese el DNI del empleado: ")
        fecha_vinculacion = input("Ingrese la fecha de vinculación del empleado: ")
        empleado = Empleado(nombre, apellido, edad, salario, dni, fecha_vinculacion)
        self.agregar_empleado(empleado)

    def ingresar_datos_jefe(self):
        nombre = input("Ingrese el nombre del jefe: ")
        apellido = input("Ingrese el apellido del jefe: ")
        edad = int(input("Ingrese la edad del jefe: "))
        salario = float(input("Ingrese el salario del jefe: "))
        dni = input("Ingrese el DNI del jefe: ")
        fecha_vinculacion = input("Ingrese la fecha de vinculación del jefe: ")
        jefe = Jefe(nombre, apellido, edad, salario, dni, fecha_vinculacion)
        self.agregar_jefe(jefe)

    def ingresar_datos_area(self):
        nombre = input("Ingrese el nombre del área: ")
        descripcion = input("Ingrese la descripción del área: ")
        area = Area(nombre, descripcion)
        self.agregar_area(area)

    def consultar_empleado_por_nombre(self, nombre_completo):
        for empleado in self.empleados:
            if empleado.obtener_nombre_completo() == nombre_completo:
                return empleado
        return None

    def consultar_empleado_por_dni(self, dni):
        for empleado in self.empleados:
            if empleado.dni == dni:
                return empleado
        return None

    def consultar_jefe_por_nombre(self, nombre_completo):
        for jefe in self.jefes:
            if jefe.obtener_nombre_completo() == nombre_completo:
                return jefe
        return None

    def consultar_jefe_por_dni(self, dni):
        for jefe in self.jefes:
            if jefe.dni == dni:
                return jefe
        return None

    def consultar_area_por_nombre(self, nombre):
        for area in self.areas:
            if area.nombre == nombre:
                return area
        return None

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

        print("Datos guardados en CSV.")

    def cargar_datos(self, archivo_empleados, archivo_jefes, archivo_areas):
        if not os.path.exists(archivo_empleados):
            with open(archivo_empleados, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Nombre', 'Apellido', 'Edad', 'Salario', 'DNI', 'Fecha de Vinculación'])

        if not os.path.exists(archivo_jefes):
            with open(archivo_jefes, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Nombre', 'Apellido', 'Edad', 'Salario', 'DNI', 'Fecha de Vinculación', 'Empleados a Cargo'])

        if not os.path.exists(archivo_areas):
            with open(archivo_areas, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Nombre Área', 'Descripción', 'Empleados'])

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
                # Asignar empleados a cargo si existen en los datos
                if len(row) > 6 and row[6]:
                    empleados_a_cargo = row[6].split(', ')
                    for nombre_empleado in empleados_a_cargo:
                        empleado = self.consultar_empleado_por_nombre(nombre_empleado)
                        if empleado:
                            jefe.agregar_empleado(empleado)
        
        with open(archivo_areas, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Saltar la primera fila que contiene los encabezados
            for row in reader:
                if len(row) < 2:
                    continue  # Ignorar filas incompletas
                area = Area(row[0], row[1])
                self.areas.append(area)
                # Asignar empleados al área si existen en los datos
                if len(row) > 2 and row[2]:
                    empleados_area = row[2].split(', ')
                    for nombre_empleado in empleados_area:
                        empleado = self.consultar_empleado_por_nombre(nombre_empleado)
                        if empleado:
                            area.agregar_empleado(empleado)

    def asignar_empleado_a_area(self):
        nombre_empleado = input("Ingrese el nombre completo del empleado (Nombre Apellido): ")
        nombre_area = input("Ingrese el nombre del área: ")
        empleado = self.consultar_empleado_por_nombre(nombre_empleado)
        area = self.consultar_area_por_nombre(nombre_area)
        if empleado and area:
            area.agregar_empleado(empleado)
            print(f"Empleado {empleado.obtener_nombre_completo()} asignado al área {area.nombre}.")
        else:
            print("Empleado o área no encontrados.")

    def asignar_area_a_jefe(self):
        nombre_area = input("Ingrese el nombre del área: ")
        nombre_jefe = input("Ingrese el nombre completo del jefe (Nombre Apellido): ")
        area = self.consultar_area_por_nombre(nombre_area)
        jefe = self.consultar_jefe_por_nombre(nombre_jefe)
        if area and jefe:
            area.jefe = jefe
            print(f"Área {area.nombre} asignada al jefe {jefe.obtener_nombre_completo()}.")
        else:
            print("Área o jefe no encontrados.")

    def consultar_empleados_por_dni(self):
        dni = input("Ingrese el DNI del empleado: ")
        empleado = self.consultar_empleado_por_dni(dni)
        if empleado:
            print(empleado)
        else:
            print(f"No se encontró un empleado con DNI {dni}.")

    def consultar_empleados_por_nombre(self):
        nombre_completo = input("Ingrese el nombre completo del empleado (Nombre Apellido): ")
        empleado = self.consultar_empleado_por_nombre(nombre_completo)
        if empleado:
            print(empleado)
        else:
            print(f"No se encontró un empleado con nombre {nombre_completo}.")

    def consultar_jefes_por_dni(self):
        dni = input("Ingrese el DNI del jefe: ")
        jefe = self.consultar_jefe_por_dni(dni)
        if jefe:
            print(jefe)
        else:
            print(f"No se encontró un jefe con DNI {dni}.")

    def consultar_jefes_por_nombre(self):
        nombre_completo = input("Ingrese el nombre completo del jefe (Nombre Apellido): ")
        jefe = self.consultar_jefe_por_nombre(nombre_completo)
        if jefe:
            print(jefe)
        else:
            print(f"No se encontró un jefe con nombre {nombre_completo}.")

    def consultar_areas_por_nombre(self):
        nombre_area = input("Ingrese el nombre del área: ")
        area = self.consultar_area_por_nombre(nombre_area)
        if area:
            print(area)
            if area.jefe:
                print(f"Jefe del área {area.nombre}: {area.jefe.obtener_nombre_completo()}")
            else:
                print(f"El área {area.nombre} no tiene un jefe asignado.")
        else:
            print(f"No se encontró un área con nombre {nombre_area}.")

    def consultar_empleados_de_area_y_su_jefe(self):
        nombre_area = input("Ingrese el nombre del área: ")
        area = self.consultar_area_por_nombre(nombre_area)
        if area:
            print(area)
            if area.jefe:
                print(f"Jefe del área {area.nombre}: {area.jefe.obtener_nombre_completo()}")
            else:
                print(f"El área {area.nombre} no tiene un jefe asignado.")
        else:
            print(f"No se encontró un área con nombre {nombre_area}.")

    def consultar_empleados_de_jefe(self):
        nombre_jefe = input("Ingrese el nombre completo del jefe (Nombre Apellido): ")
        jefe = self.consultar_jefe_por_nombre(nombre_jefe)
        if jefe:
            empleados_a_cargo = jefe.listar_empleados_a_cargo()
            if empleados_a_cargo:
                print(f"Empleados a cargo de {jefe.obtener_nombre_completo()}: {', '.join(empleados_a_cargo)}")
            else:
                print(f"El jefe {jefe.obtener_nombre_completo()} no tiene empleados a cargo.")
        else:
            print(f"No se encontró un jefe con nombre {nombre_jefe}.")

    def consultar_empleados_de_area(self):
        nombre_area = input("Ingrese el nombre del área: ")
        area = self.consultar_area_por_nombre(nombre_area)
        if area:
            empleados_area = area.listar_empleados()
            if empleados_area:
                print(f"Empleados del área {area.nombre}: {', '.join(empleados_area)}")
            else:
                print(f"El área {area.nombre} no tiene empleados asignados.")
        else:
            print(f"No se encontró un área con nombre {nombre_area}.")

    def consultar_salario_de_empleado_por_dni(self):
        dni = input("Ingrese el DNI del empleado: ")
        empleado = self.consultar_empleado_por_dni(dni)
        if empleado:
            print(f"Salario del empleado {empleado.obtener_nombre_completo()}: {empleado.salario}")
        else:
            print(f"No se encontró un empleado con DNI {dni}.")

def main():
    sistema = SistemaGestionEmpleados()
    sistema.cargar_datos('empleados.csv', 'jefes.csv', 'areas.csv')

    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Agregar Área")
        print("2. Agregar Empleado")
        print("3. Agregar Jefe de Área")
        print("4. Asignar Área a Jefe")
        print("5. Asignar Empleados a Área")
        print("6. Guardar Datos")
        print("7. Consultar Empleados por DNI")
        print("8. Consultar Empleados por Nombre")
        print("9. Consultar Jefes por DNI")
        print("10. Consultar Jefes por Nombre")
        print("11. Consultar Áreas por Nombre")
        print("12. Consultar Empleados de un Área y su Jefe")
        print("13. Consultar Empleados de un Jefe")
        print("14. Consultar Empleados de un Área")
        print("15. Consultar Salario de un Empleado por DNI")
        print("16. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            sistema.ingresar_datos_area()
        elif opcion == '2':
            sistema.ingresar_datos_empleado()
        elif opcion == '3':
            sistema.ingresar_datos_jefe()
        elif opcion == '4':
            sistema.asignar_area_a_jefe()
        elif opcion == '5':
            sistema.asignar_empleado_a_area()
        elif opcion == '6':
            sistema.guardar_datos('empleados.csv', 'jefes.csv', 'areas.csv')
        elif opcion == '7':
            sistema.consultar_empleados_por_dni()
        elif opcion == '8':
            sistema.consultar_empleados_por_nombre()
        elif opcion == '9':
            sistema.consultar_jefes_por_dni()
        elif opcion == '10':
            sistema.consultar_jefes_por_nombre()
        elif opcion == '11':
            sistema.consultar_areas_por_nombre()
        elif opcion == '12':
            sistema.consultar_empleados_de_area_y_su_jefe()
        elif opcion == '13':
            sistema.consultar_empleados_de_jefe()
        elif opcion == '14':
            sistema.consultar_empleados_de_area()
        elif opcion == '15':
            sistema.consultar_salario_de_empleado_por_dni()
        elif opcion == '16':
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
