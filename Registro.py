from Manejo_Datos import *

def registro_ciudades():
    cargar_datos()
    data = {}
    Codigo_Postal = input("Ingresa el codigo postal de la ciudad:  ")
    if not validar_codigo(Codigo_Postal):
        data["Nombre"] = input("Ingresa el nombre de la ciudad: ").upper()
        data["Poblacion"] = int(input("Ingresa la poblacion estimada de la ciudad: "))
        data["Pais"] = input("Ingresa el pais de la ciudad: ").upper()
        Ciudades[Codigo_Postal] = data
    else:
        print("La ciudad ya existe")
    guardar_datos()


def validar_codigo(codigo):
    for Categoria in Ciudades.keys():
        if codigo in Categoria:
            return True
    return False


def modificar_ciudad():
    cargar_datos()

    Codigo_Postal = input("Ingresa el codigo postal de la ciudad:  ")
    if Codigo_Postal not in Ciudades:
        print("-"*60)
        print("         La ciudad no existe")
        print("-"*60)
    else:
        print("¿Qué valor desea modificar?")
        print("1. Nombre")
        print("2. Poblacion")
        print("3. Pais")
        print("4. Modificar todos")
        try:
            opcion = int(input("Ingresa el número de la opción: "))
            if opcion == 1:
                Ciudades[Codigo_Postal ]['Nombre'] = input("Ingresa el nuevo nombre: ").upper()
            elif opcion == 2:
                Ciudades[Codigo_Postal ]['Poblacion'] = int(input("Ingresa el nuevo poblacion estimada: "))
            elif opcion == 3:
                Ciudades[Codigo_Postal ]['Pais'] = input("Ingresa el nuevo pais: ").upper()
            elif opcion == 4:
                Ciudades[Codigo_Postal ]['Nombre'] = input("Ingresa el nuevo nombre: ").upper()
                Ciudades[Codigo_Postal ]['Poblacion'] = int(input("Ingresa el nuevo poblacion estimada: "))
                Ciudades[Codigo_Postal ]['Pais'] = input("Ingresa el nuevo pais: ").upper()
                print("-"*60)
                print("Datos Actualizados")
                print("-"*60)
                
            else:
                print("Opción no válida")
        except Exception as e:
            print("-"*60)
            print(f"ERROR ")
            print("-"*60)
        guardar_datos()

def Eliminar_ciudades():
    cargar_datos()

    Codigo_Postal = input("Ingresa el codigo postal de la ciudad:  ")
    if Codigo_Postal not in Ciudades:
        print("-"*30)
        print("     La ciudad no existe")
        print("-"*30)
    else:   
        Ciudades.pop(Codigo_Postal)
        print("-"*30)
        print(f"Ciudad Eliminada ")
        print("-"*30)
    guardar_datos()
