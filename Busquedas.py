from Manejo_Datos import *

def mostrar_ciudades(): 
    cargar_datos()
    print("************************************************************")
    print("                   REPORTE CIUDADES ")
    print("************************************************************\n")

    print(f"{'CODIGO POSTAL':<15} {'NOMBRE':<15} {'POBLACIÓN':<15} {'PAÍS':<15}")
    print("-"*60)
    for codigo, informacion in Ciudades.items():
        print(f"{codigo:<15} {informacion['Nombre']:<15} {informacion['Poblacion']:<15} {informacion['Pais']:<15}\n")
