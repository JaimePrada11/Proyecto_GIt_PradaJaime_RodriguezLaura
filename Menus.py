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

def menu_principal(): 
    while True: 
        print("¡Bienvenido al menú de ciudades!")
        opcion = recorrer_opciones(opciones_principal)
        if opcion == "1": 
            clear_consola()
            print("Esta en la opcion 1")
        elif opcion == "2": 
            clear_consola()
            print("Esta en la opcion 2")
        elif opcion == "3": 
            clear_consola()
            print("Esta en la opcion 3")
        elif opcion == "4": 
            clear_consola()
            menu_busquedas()
        elif opcion == "5": 
            clear_consola()
            print("Esta en la opcion 5")
            break
        else: 
            clear_consola()
            print("Opción incorrecta, por favor ingrese un valor válido")

def menu_busquedas(): 
    while True: 
        print("¡Bienvenido al menú de busquedas!")
        opcion = recorrer_opciones(opciones_busqueda)
        if opcion == "1": 
            clear_consola()
            print("Esta en la opcion 1")
        elif opcion == "2": 
            clear_consola()
            print("Esta en la opcion 2")
        elif opcion == "3": 
            clear_consola()
            print("Esta en la opcion 3")
            break
        else: 
            clear_consola()
            print("Opción incorrecta, por favor ingrese un valor válido")

menu_principal()