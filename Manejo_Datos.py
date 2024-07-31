import json

Ciudades = {}

Ruta = "Data_Base/Informacion.json" 

def guardar_datos():
    try:
        with open(Ruta, "w", encoding='utf-8') as file:
            json.dump(Ciudades, file, indent=4, ensure_ascii=False  )
    except Exception as e:
        print(f"Error {e}")


def cargar_datos():
    try:
        with open(Ruta, "r", encoding='utf-8') as archivo:
            Ciudades.update(json.load(archivo))
    except Exception as e:
        print(f"Error al cargar datos {e}")
