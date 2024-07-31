import os
from Busquedas import *

def clear_consola(): 
    os.system("clear")

opciones_principal = ("1. Crear una nueva ciudad", "2. Eliminar una ciudad", "3. Actualizar una ciudad", "4. Buscar ciudades", "5. Salir del programa")
opciones_busqueda = ("1. Ver todas las ciudades", "2. Usar filtros para buscar ciudades", "3. Salir del menú")

def recorrer_opciones(opciones):
    for opcion in opciones: 
        print(opcion)
    opcion = input("Por favor, ingrese una opción: ")
    return opcion

def menu_principal(): 
    while True: 
        print("************************************************************")
        print("               ¡BIENVENIDO AL MENÚ DE CIUDADES ")
        print("************************************************************\n")
        opcion = recorrer_opciones(opciones_principal)
        if opcion == "1": 
            clear_consola()
            #registro_ciudades()
        elif opcion == "2": 
            clear_consola()
            #eliminar_ciudades()
        elif opcion == "3": 
            clear_consola()
            print("Esta en la opcion 3")
        elif opcion == "4": 
            clear_consola()
            menu_busquedas()
        elif opcion == "5": 
            clear_consola()
            break
        else: 
            clear_consola()
            print("Opción incorrecta, ingrese un valor válido")

def menu_busquedas(): 
    while True: 
        print("************************************************************")
        print("            ¡BIENVENIDO AL MENÚ DE BÚSQUEDAS ")
        print("************************************************************\n")
        opcion = recorrer_opciones(opciones_busqueda)
        if opcion == "1": 
            clear_consola()
            mostrar_ciudades()
        elif opcion == "2": 
            clear_consola()
            mostrar_ciudades_filtro()
        elif opcion == "3": 
            clear_consola()
            break
        else: 
            clear_consola()
            print("Opción incorrecta, ingrese un valor válido")

menu_principal()