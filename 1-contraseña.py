import random
import string
import os

# genera la contraseña segura
def generar_contrasena():
    longitud = 10 # Longitud de la contraseña
    letras = string.ascii_letters # contiene las letras del alfabeto en mayús. y minús.
    numeros = string.digits # contiene los números del 0 al 9
    caracteres_especiales = string.punctuation  # contiene los caracteres especiales
    # combina las letras, números y caracteres especiales
    combinacion = letras + numeros + caracteres_especiales
    # selección aleatoria de los caracteres para crear la contraseña
    contrasena = ''.join(random.choice(combinacion) for i in range(longitud)) # para evitar espacios en blanco se coloca cadena vacía ''
    return contrasena

# verificar las condiciones de la contraseña
def condiciones_contrasena(contrasena):
    return (len(contrasena) >= 8 and
            not ' ' in contrasena and
            any(char.isupper() for char in contrasena) and
            any(char.islower() for char in contrasena) and
            any(char.isdigit() for char in contrasena) and
            any(char in string.punctuation for char in contrasena))

# genera la contraseña segura y la guarda en un archivo txt
def guardar_contrasena():
    contrasena = generar_contrasena()
    while not condiciones_contrasena(contrasena):   # se ejecuta hasta que la contraseña cumpla las condiciones
        contrasena = generar_contrasena()
    with open('contrasena.txt', 'a') as file:   # crea el archivo y agrega contenido al final (sin reescribir)
        file.write(contrasena + '\n')
    print("La contraseña generada es:", contrasena)     # muestra la contraseña en consola

# ejecuta la función guardar contraseña
guardar_contrasena()

# muestra la carpeta en la que se guardó el txt con la contraseña
carpeta = os.getcwd()
print("La carpeta en la que se guardó el archivo es:", carpeta)