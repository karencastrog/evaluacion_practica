# Función para contar las líneas del archivo
def contar_lineas(archivo):
    with open(archivo, 'r') as file:
        return sum(1 for line in file)

# Función para contar las palabras del archivo
def contar_palabras(archivo):
    with open(archivo, 'r') as file:
        total_palabras = 0       # Inicializa un contador de palabras
        for line in file:
            palabras = line.split()     # Divide la línea en palabras 
            total_palabras += len(palabras)     # Incrementa el contador según cantidad de palabras
        return total_palabras

# Función para contar los caracteres del archivo
def contar_caracteres(archivo):
    with open(archivo, 'r') as file:
        caracteres = file.read()
        return len(caracteres)

# Función para contar palabras repetidas
def contar_palabras_repetidas(archivo):
    with open(archivo, "r") as file:
        texto = file.read().lower()

        # Reemplazar los caracteres especiales y números
        reemplazar = "-*?¿,;:.¡!\"'0123456789"
        for palabra in reemplazar:
            texto = texto.replace(palabra, "")
        palabras = texto.split()
        diccionario_repetidas = {}

        for palabra in palabras:
            if palabra in diccionario_repetidas: 
                diccionario_repetidas[palabra] += 1
            else:
                diccionario_repetidas[palabra] = 1    
        return diccionario_repetidas 
    
# Archivo de entrada
archivo_entrada = 'texto.txt'
print("se abrió el archivo texto.txt")

# Archivo de salida
archivo_salida = 'resultado.txt'

# Contar líneas
lineas_totales = contar_lineas(archivo_entrada)

# Contar palabras
palabras_totales = contar_palabras(archivo_entrada)

# Contar caracteres
caracteres_totales = contar_caracteres(archivo_entrada)

# Contar palabras repetidas
palabras_repetidas = contar_palabras_repetidas(archivo_entrada)

# Escribir los resultados en el archivo de salida
with open(archivo_salida, 'w') as file:
    file.write(f"Líneas totales: {lineas_totales}\n")
    file.write(f"Palabras totales: {palabras_totales}\n")
    file.write(f"Caracteres totales: {caracteres_totales}\n")
    file.write(f"Palabras repetidas:\n")
    for palabra in palabras_repetidas:
        frecuencia = palabras_repetidas[palabra]
        if frecuencia >= 2:
            file.write(f"La palabra '{palabra}' tiene una frecuencia de: {frecuencia}\n")
print("se generó el archivo resultado.txt")