import os

def clear_consola(): 
    os.system("clear")

opciones_principal = ("1. Crear una nueva ciudad", "2. Eliminar una ciudad", "3. Actualizar una ciudad", "4. Buscar ciudades", "5. Salir del programa")
opciones_busqueda = ("1. Ver todas las ciudades", "2. Usar filtros para buscar ciudades", "3. Salir del menú")

def recorrer_opciones(opciones):
    for opcion in opciones: 
        print(opcion)
    opcion = input("Por favor ingrese la opcion seleccionada: ")
    return opcion
