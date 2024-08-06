# Importaciones
import json

# Clase Base

class Producto:

    # Asignacion de codigo unico
    __codigo_unico = 1

    def __init__(self, nombre, precio, cantidad):
        self.codigo_unico = Producto.__codigo_unico
        Producto.__codigo_unico += 1
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def a_diccionario(self):
        return {
            "codigo":self.codigo_unico,
            "nombre":self.nombre,
            "precio":self.precio,
            "cantidad":self.cantidad
        }

# Clases Derivadas

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, cantidad, es_electronico):
        super().__init__(nombre, precio, cantidad)
        self.es_electronico = es_electronico
    
    def a_diccionario(self):
        dato = super().a_diccionario()
        dato["es_electronico"] = self.es_electronico
        return dato

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, cantidad, vencimiento):
        super().__init__(nombre, precio, cantidad)
        self.vencimiento = vencimiento

    def a_diccionario(self):
        dato = super().a_diccionario()
        dato["vencimiento"] = self.vencimiento
        return dato

class ProductoVestimenta(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
    
    def a_diccionario(self):
        dato = super().a_diccionario()
        dato["talla"] = self.talla
        return dato

# Operaciones CRUD

class GestionProductos:
    def __init__(self, archivo):
        self.archivo = archivo
    
    def leer_archivo(self):
        try:
            with open(self.archivo, "r") as file:
                datos = json.load(file)
        
        except Exception as error:
            raise Exception(f"Error al cargar los datos del archivo: {error}")
        
        return datos
    
    def guardar_archivo(self, datos):
        try:
            with open(self.archivo, "w") as file:
                json.dump(datos, file, indent=4)
        
        except Exception as error:
            raise Exception(f"Error al guardar los datos en el archivo: {error}")
    
    def crear_producto(self, producto):
        try:
            datos = self.leer_archivo()

        
        except Exception as error:
            raise Exception(f"Error inesperado: {error}")