from Manejo_Datos import *

def registro_ciudades():
    cargar_datos()
    data = {}
    while True:
        Codigo_Postal = input("Ingresa el codigo postal de la ciudad:  ").strip()
        if Codigo_Postal:
            break
        else:
            print("No puede estar vacio")
            
    if not validar_codigo(Codigo_Postal):
        while True:
            nombre = input("Ingresa el nombre de la ciudad: ").strip()
            if nombre:
                data["Nombre"] = nombre.upper()
                break
            else:
                print("EL nombre no puede estar vacía. Por favor, ingresa un nombre valido.")
        while True:
            try:
                data["Poblacion"] = int(input("Ingresa la poblacion estimada de la ciudad: "))
                break
            except Exception:
                print("El valor debe ser un numero")
        while True:
            pais = input("Ingresa el pais de la ciudad: ").strip()
            if pais:
                data["Pais"] = pais.upper()
                break
            else:
                print("El pais no puede estar vacía. Por favor, ingresa un pais.")
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
                while True:
                    nombre = input("Ingresa el nuevo nombre de la ciudad: ").strip()
                    if nombre:
                        Ciudades[Codigo_Postal]["Nombre"] = nombre.upper()
                        break
                    else:
                        print("El nombre no puede estar vacía. Por favor, ingresa un nombre valido.")
            elif opcion == 2:
                while True:
                    try:
                        Ciudades[Codigo_Postal]["Poblacion"] = int(input("Ingresa la nueva poblacion estimada de la ciudad: "))
                        break
                    except Exception:
                        print("El valor debe ser un numero")
            elif opcion == 3:
                while True:
                    pais = input("Ingresa el nuevo pais de la ciudad: ").strip()
                    if pais:
                        Ciudades[Codigo_Postal]["Pais"] = pais.upper()
                        break
                    else:
                        print("El pais no puede estar vacía. Por favor, ingresa un pais.")

            elif opcion == 4:
                while True:
                    nombre = input("Ingresa el nuevo nombre de la ciudad: ").strip()
                    if nombre:
                        Ciudades[Codigo_Postal]["Nombre"] = nombre.upper()
                        break
                    else:
                        print("El nombre no puede estar vacía. Por favor, ingresa un nombre valido.")
                while True:
                    try:
                        Ciudades[Codigo_Postal]["Poblacion"] = int(input("Ingresa nueva poblacion estimada de la ciudad: "))
                        break
                    except Exception:
                        print("El valor debe ser un numero")
                while True:
                    pais = input("Ingresa el nuevo pais de la ciudad: ").strip()
                    if pais:
                        Ciudades[Codigo_Postal]["Pais"] = pais.upper()
                        break
                    else:
                        print("El pais no puede estar vacía. Por favor, ingresa un pais.")
                print("-"*60)
                print("Datos Actualizados")
                print("-"*60)
            else:
                print("-"*60)
                print("Opcion Invalida")
                print("-"*60)

        except Exception:
            print("-"*60)
            print(f"DATO ERRADO")
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
