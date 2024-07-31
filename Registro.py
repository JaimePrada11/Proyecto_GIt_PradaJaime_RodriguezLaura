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

