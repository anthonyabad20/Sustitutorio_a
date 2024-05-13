
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.__nombre = nombre
        self.edad = edad
        self.ciudad = ciudad



    def imprimir(self):
        print("Su nombre es ", self.__nombre)
        print("Su edad es ", self.edad)
        print("Su ciudad es ", self.ciudad)


class Empleado(Persona):
    def __init__(self, nombre, edad, ciudad):
        super().__init__(nombre,edad,ciudad)
        self.sueldo = 0


    def intro_sueld(self):
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))


    def calc_impuest(self):
        self.impuesto = 0
        if self.sueldo > 5500 :
            self.impuesto = 0.09 * self.sueldo
            print("El impuesto que tiene que pagar es de {} soles".format(self.impuesto))

        else:
            print("Ud. No tiene que pagar impuesto")


    def manejoDiccionario(self):
        diccionario = {
            "nombre": self._Persona__nombre,
            "edad": self.edad,
            "ciudad": self.ciudad,
            "sueldo": self.sueldo,
            "impuesto": self.impuesto
        }
        print("Los valores del diccionario son ", diccionario)


    def generarArchivoEmpleado(self):
        with open("empleados.txt", "a") as archivo:
            archivo.write(f"{self._Persona__nombre},{self.sueldo},{self.impuesto}\n")


    def encontrar_empleados(sel, nombre_empleado):
        with open("empleados.txt", "r") as archivo:
            for linea in archivo:
                nombre, sueldo, impuesto = linea.strip().split(",")
                if nombre == nombre_empleado:
                    print("El empleado {} tiene una remuneración de {} soles y un impuesto de {} soles".format(nombre, sueldo , impuesto))
                    return
                else:
                    print("\nNo se encontro ningun empledo con el nombre {}".format(nombre_empleado))

nombre = input("Ingrese el nombre del empleado: ")
edad = int(input("Ingrese la edad del empleado: "))
ciudad = input("Ingrese la ciudad del empleado: ")


per_01 = Empleado("Anthony", 15, "Piura")
per_01.intro_sueld()
per_01.calc_impuest()
per_01.imprimir()
per_01.generarArchivoEmpleado()
per_01.manejoDiccionario()
nombre_a_buscar=input("\nIngrese el nombre del empleado a buscar:")
per_01.encontrar_empleados(nombre_a_buscar)










