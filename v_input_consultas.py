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
        self.jefe = None
        self.area = None

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
        empleado.jefe = self

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
        empleado.area = self

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

    # Nuevos métodos de consulta
    def quien_es_el_jefe_de(self, nombre_completo):
        empleado = self.consultar_empleado_por_nombre(nombre_completo)
        if empleado and empleado.jefe:
            return empleado.jefe.obtener_nombre_completo()
        return "No se encontró el empleado o no tiene jefe"

    def en_que_area_trabaja(self, dni):
        empleado = self.consultar_empleado_por_dni(dni)
        if empleado and empleado.area:
            return empleado.area.nombre
        return "No se encontró el empleado o no está asignado a un área"

    def cuantos_empleados_en_area(self, nombre_area):
        area = self.consultar_area_por_nombre(nombre_area)
        if area:
            return len(area.empleados)
        return "No se encontró el área"

    def cuales_empleados_en_area(self, nombre_area):
        area = self.consultar_area_por_nombre(nombre_area)
        if area:
            return area.listar_empleados()
        return "No se encontró el área"

    def cuantos_empleados_a_cargo_de(self, nombre_completo_o_dni):
        jefe = self.consultar_jefe_por_nombre(nombre_completo_o_dni)
        if not jefe:
            jefe = self.consultar_jefe_por_dni(nombre_completo_o_dni)
        if jefe:
            return len(jefe.empleados_a_cargo)
        return "No se encontró el jefe"

    def cuales_empleados_a_cargo_de(self, nombre_completo_o_dni):
        jefe = self.consultar_jefe_por_nombre(nombre_completo_o_dni)
        if not jefe:
            jefe = self.consultar_jefe_por_dni(nombre_completo_o_dni)
        if jefe:
            return jefe.listar_empleados_a_cargo()
        return "No se encontró el jefe"

    def cual_es_el_salario_de(self, nombre_completo_o_dni):
        empleado = self.consultar_empleado_por_nombre(nombre_completo_o_dni)
        if not empleado:
            empleado = self.consultar_empleado_por_dni(nombre_completo_o_dni)
        if empleado:
            return empleado.salario
        return "No se encontró el empleado"

    def asignar_empleado_a_area(self):
        nombre_empleado = input("Ingrese el nombre completo del empleado (Nombre Apellido): ")
        nombre_area = input("Ingrese el nombre del área: ")
        empleado = self.consultar_empleado_por_nombre(nombre_empleado)
        area = self.consultar_area_por_nombre(nombre_area)
        if empleado and area:
            area.agregar_empleado(empleado)
            print(f"Empleado {empleado.obtener_nombre_completo()} asignado al área {area.nombre}")
        else:
            print("Empleado o área no encontrados")

    def asignar_jefe_a_empleado(self):
        nombre_empleado = input("Ingrese el nombre completo del empleado (Nombre Apellido): ")
        nombre_jefe = input("Ingrese el nombre completo del jefe (Nombre Apellido): ")
        empleado = self.consultar_empleado_por_nombre(nombre_empleado)
        jefe = self.consultar_jefe_por_nombre(nombre_jefe)
        if empleado and jefe:
            jefe.agregar_empleado(empleado)
            print(f"Empleado {empleado.obtener_nombre_completo()} asignado al jefe {jefe.obtener_nombre_completo()}")
        else:
            print("Empleado o jefe no encontrados")

# Ejemplo de uso
def main():
    sistema = SistemaGestionEmpleados()

    while True:
        print("\nSistema de Gestión de Empleados")
        print("1. Ingresar datos de un empleado")
        print("2. Ingresar datos de un jefe")
        print("3. Ingresar datos de un área")
        print("4. Consultar empleado por nombre")
        print("5. Consultar empleado por DNI")
        print("6. Guardar datos en archivos CSV")
        print("7. Cargar datos desde archivos CSV")
        print("8. Asignar empleado a área")
        print("9. Asignar jefe a empleado")
        print("10. ¿Quién es el jefe de un empleado?")
        print("11. ¿En qué área trabaja el empleado?")
        print("12. ¿Cuántos empleados hay en un área?")
        print("13. ¿Cuáles empleados hay en un área?")
        print("14. ¿Cuántos empleados tiene a cargo el jefe?")
        print("15. ¿Cuáles empleados tiene a cargo el jefe?")
        print("16. ¿Cuál es el salario del empleado?")
        print("17. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.ingresar_datos_empleado()
        elif opcion == "2":
            sistema.ingresar_datos_jefe()
        elif opcion == "3":
            sistema.ingresar_datos_area()
        elif opcion == "4":
            nombre = input("Ingrese el nombre completo del empleado (Nombre Apellido): ")
            empleado = sistema.consultar_empleado_por_nombre(nombre)
            if empleado:
                print(empleado)
            else:
                print("Empleado no encontrado")
        elif opcion == "5":
            dni = input("Ingrese el DNI del empleado: ")
            empleado = sistema.consultar_empleado_por_dni(dni)
            if empleado:
                print(empleado)
            else:
                print("Empleado no encontrado")
        elif opcion == "6":
            sistema.guardar_datos("empleados.csv", "jefes.csv", "areas.csv")
        elif opcion == "7":
            sistema.cargar_datos("empleados.csv", "jefes.csv", "areas.csv")
        elif opcion == "8":
            sistema.asignar_empleado_a_area()
        elif opcion == "9":
            sistema.asignar_jefe_a_empleado()
        elif opcion == "10":
            nombre = input("Ingrese el nombre completo del empleado (Nombre Apellido): ")
            print(sistema.quien_es_el_jefe_de(nombre))
        elif opcion == "11":
            dni = input("Ingrese el DNI del empleado: ")
            print(sistema.en_que_area_trabaja(dni))
        elif opcion == "12":
            nombre_area = input("Ingrese el nombre del área: ")
            print(sistema.cuantos_empleados_en_area(nombre_area))
        elif opcion == "13":
            nombre_area = input("Ingrese el nombre del área: ")
            print(sistema.cuales_empleados_en_area(nombre_area))
        elif opcion == "14":
            nombre_o_dni = input("Ingrese el nombre completo o DNI del jefe: ")
            print(sistema.cuantos_empleados_a_cargo_de(nombre_o_dni))
        elif opcion == "15":
            nombre_o_dni = input("Ingrese el nombre completo o DNI del jefe: ")
            print(sistema.cuales_empleados_a_cargo_de(nombre_o_dni))
        elif opcion == "16":
            nombre_o_dni = input("Ingrese el nombre completo o DNI del empleado: ")
            print(sistema.cual_es_el_salario_de(nombre_o_dni))
        elif opcion == "17":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
