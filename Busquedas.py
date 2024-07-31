from Manejo_Datos import *

def mostrar_ciudades(): 
    cargar_datos()
    print("************************************************************")
    print("                   REPORTE CIUDADES ")
    print("************************************************************\n")

    if not Ciudades:
        print("No hay ciudades registradas")
        return

    print(f"{'CODIGO POSTAL':<15} {'NOMBRE':<15} {'POBLACIÓN':<15} {'PAÍS':<15}")
    print("-"*60)
    for codigo, informacion in Ciudades.items():
        print(f"{codigo:<15} {informacion['Nombre']:<15} {informacion['Poblacion']:<15} {informacion['Pais']:<15}\n")

def mostrar_ciudades_filtro(): 
    cargar_datos()
    print("************************************************************")
    print(f"           REPORTE CIUDADES")
    print("************************************************************\n")

    if not Ciudades: 
        print("No hay ciudades disponibles")
        return 
    
    print("Opciones de búsqueda: ")
    print("1. Código postal")
    print("2. Nombre")
    print("3. Población")
    print("4. País")
    

    opciones_busqueda = {
        "1": "Código postal",
        "2": "Nombre",
        "3": "Poblacion",
        "4": "Pais",
    }
    
    while True: 
        opcion = input("Seleccione una opción de búsqueda o escriba '0' para salir: ")
        if opcion == "0":
            return
        if opcion in opciones_busqueda:
            break
        print("Opción incorrecta. Ingrese un valor válido")
    
    while True:
        if opcion == "1":
            codigo_usuario = input("Ingrese el codigo postal de la ciudad: ")
            ciudad = Ciudades[codigo_usuario]
            if codigo_usuario in Ciudades.keys():
                print(f"{'CODIGO POSTAL':<15} {'NOMBRE':<15} {'POBLACIÓN':<15} {'PAÍS':<15}")
                print(f"{codigo_usuario:<15} {ciudad['Nombre']:<15} {ciudad['Poblacion']:<15} {ciudad['Pais']:<15}\n")
                print("-"*60)
                return
            else:
                print("El código postal no se encuentra registrado")
                return
        elif opcion == "2":
            nombre = input("Ingrese el nombre de la ciudad: ").upper()
            print(f"{'CODIGO POSTAL':<15} {'NOMBRE':<15} {'POBLACIÓN':<15} {'PAÍS':<15}")
            print("-"*60)
            for codigo, informacion in Ciudades.values():
                if nombre in informacion:
                    print(f"{codigo:<15} {informacion['Nombre']:<15} {informacion['Poblacion']:<15} {informacion['Pais']:<15}\n")
                    return
                else:
                    print("La ciudad no se encuentra registrada")
                    return
        elif opcion == "3":
            poblacion = input("Ingrese el tamaño de la poblacion: ")
            while True: 
                opcion = input("Ingrese '+' si desea que la poblacion sea mayor o '-' si desea que sea menor: ")
                if opcion == "+":
                    print(f"{'CODIGO POSTAL':<15} {'NOMBRE':<15} {'POBLACIÓN':<15} {'PAÍS':<15}")
                    print("-"*60)
                    for codigo, informacion in Ciudades.items():
                        if poblacion in informacion['Poblacion']>poblacion:
                            print(f"{codigo:<15} {informacion['Nombre']:<15} {informacion['Poblacion']:<15} {informacion['Pais']:<15}\n")
                        else:
                            print("No hay ciudades con poblaciones mayores a ese numero")
                            return
                if opcion == "-":
                    print(f"{'CODIGO POSTAL':<15} {'NOMBRE':<15} {'POBLACIÓN':<15} {'PAÍS':<15}")
                    print("-"*60)
                    for codigo, informacion in Ciudades.items():
                        if poblacion in informacion['Poblacion'] > poblacion:
                            print(f"{codigo:<15} {informacion['Nombre']:<15} {informacion['Poblacion']:<15} {informacion['Pais']:<15}\n")
                        else:
                            print("No hay ciudades con poblaciones menores a ese numero")
                            return
        elif opcion == "4":
            pais = input("Ingrese el nombre del pais: ").upper()
            print(f"{'CODIGO POSTAL':<15} {'NOMBRE':<15} {'POBLACIÓN':<15} {'PAÍS':<15}")
            print("-"*60)
            for codigo, informacion in Ciudades.items():
                if pais in informacion['Pais']:
                    print(f"{codigo:<15} {informacion['Nombre']:<15} {informacion['Poblacion']:<15} {informacion['Pais']:<15}\n")
                else:
                    print("No se encuentran ciudades registradas con ese país")
                    return
            return
        else: 
            print("Opcion invalida. Ingrese un valor correcto")
        













  
 

