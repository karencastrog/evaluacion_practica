import pyttsx3
import os

# Crea una instancia del motor de texto a voz
motor = pyttsx3.init()

# Define la ruta y nombre del archivo de entrada
archivo_entrada = "texto-entrada.txt"


# Lee el contenido del archivo
with open(archivo_entrada, "r") as file:
    contenido = file.read()

# Configura la velocidad de lectura
velocidad = motor.getProperty("rate")
motor.setProperty("rate", velocidad - 50)

# Inicia el proceso de conversión de texto a voz
motor.say(contenido)

# Ejecuta el proceso de conversión
motor.runAndWait()

# Guarda el archivo de salida en formato de audio
archivo_salida = "audio.mp3"
motor.save_to_file(contenido, archivo_salida)

# Obtiene el directorio del archivo de entrada
directorio = os.path.dirname(os.path.abspath(archivo_entrada))

# Define la ruta y nombre del archivo de salida
ruta_salida = os.path.join(directorio, archivo_salida)

# Guarda el archivo de salida en formato de audio
motor.save_to_file(contenido, ruta_salida)

# Cierra la instancia del motor de texto a voz
motor.stop()
