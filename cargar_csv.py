import csv

# Nombre del archivo CSV que contiene los datos
archivo_csv = r'C:\xampp\htdocs\analisis_dato_python\datos.csv' # ruta del csv

# Definimos una función para cargar el archivo CSV con el separador correcto
def cargar_datos_csv(archivo_csv):
    datos = []
    with open(archivo_csv, 'r', newline='') as file:
        lector_csv = csv.DictReader(file, delimiter=';')  # Especificamos el separador como ';'
        for fila in lector_csv:
            datos.append(fila)
    return datos

# Cargamos los datos desde el archivo CSV
datos = cargar_datos_csv(archivo_csv)

# Definimos una función para listar nombres únicos de la columna "CANDIDATO"
def listar_candidatos_unicos(datos):
    candidatos_unicos = set()
    for fila in datos:
        candidatos_unicos.add(fila['CANDIDATO'])
    return list(candidatos_unicos)


# Consulta 1: Listar nombres únicos de la columna "CANDIDATO"
nombres_candidatos_unicos = listar_candidatos_unicos(datos)
print("Nombres únicos de candidatos:")
for candidato in nombres_candidatos_unicos:
    print(candidato)


# Definimos una función para sumar el total de votaciones agrupado por "CORPORACION"
def sumar_votaciones_por_corporacion(datos):
    votos_por_corporacion = {}
    for fila in datos:
        corporacion = fila['CORPORACION']
        votos = int(fila['VOTACION'])
        if corporacion in votos_por_corporacion:
            votos_por_corporacion[corporacion] += votos
        else:
            votos_por_corporacion[corporacion] = votos
    return votos_por_corporacion
    
# Consulta 2: Sumar el total de votaciones agrupado por "CORPORACION"
votos_por_corporacion = sumar_votaciones_por_corporacion(datos)
print("\nTotal de votaciones por corporación:")
for corporacion, votos in votos_por_corporacion.items():
    print(f"{corporacion}: {votos} votos")

input("Presiona Enter para salir...")
