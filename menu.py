# Importaciones
import json
import os
from clases import ProductoElectronico, ProductoAlimenticio, ProductoVestimenta, GestionProductos

# Funciones

def mostrar_menu():
    print("""
#######################
    INVENTARIO 2.0    
#######################

    1. Ver INVENTARIO
    2. Agregar PRODUCTO
    3. Buscar PRODUCTO
    4. Actualizar PRODUCTO
    5. Eliminar PRODUCTO
    6. Salir

""")

def limpiar():
    os.system("cls") #Windows

def listar_inventario(gestion):
    limpiar()
    print("""
###################
    Inventario    
###################
""")
    inventario = gestion.leer_archivo()
    for producto in inventario:
        print(producto)

def agregar_producto():
    limpiar()
    print("""
########################
    Agregar PRODUCTO
########################
""")
    tipo = input("Es un producto electronico? S/N: ").capitalize()
    if tipo not in ["S", "N"]:
        print("Opcion no válida, ingrese S(SI) o N(NO)")

def buscar_producto():
    pass

def actualizar_producto():
    pass

def eliminar_producto():
    pass

# Menu

if __name__ == "__main__":

    archivo = "inventario.json"

    if not os.path.exists(archivo):
        with open(archivo, "w") as file:
            json.dump([], file)
    
    gestion = GestionProductos(archivo)

    while True:
        limpiar()
        mostrar_menu()
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                listar_inventario(gestion)
                input("Presione ENTER para continuar.")
            elif opcion == 2:
                agregar_producto()
            elif opcion == 3:
                buscar_producto()
            elif opcion == 4:
                actualizar_producto()
            elif opcion == 5:
                eliminar_producto()
            elif opcion == 6:
                limpiar()
                break
            else:
                limpiar()
                print("Selecciona una opción válida.")
                input("Presiona ENTER para continuar.")
        
        except ValueError:
            limpiar()
            print("Selecciona una opcion válida.")
            input("Presiona ENTER para continuar.")
        
        except Exception as error:
            raise Exception(f"Error inesperado {error}")