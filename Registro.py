from Manejo_Datos import *

def registro_ciudades():
    cargar_datos()
    data = {}
    Codigo_Postal = input("Ingresa el codigo postal de la ciudad:  ")
    data["Nombre"] = input("Ingresa el nombre de la ciudad: ").upper()
    data["Poblacion"] = int(input("Ingresa la poblacion estimada de la ciudad: "))
    data["Pais"] = input("Ingresa el pais de la ciudad: ").upper()
    Ciudades[Codigo_Postal] = data
    guardar_datos()
