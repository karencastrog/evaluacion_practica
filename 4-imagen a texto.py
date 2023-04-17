import pytesseract
import translator


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Karen\appdata\local\programs\python\python311\lib\site-packages'

# Configura el idioma de origen y destino
idioma_origen = 'eng'
idioma_destino = 'es'

# Lee la imagen y conviértela a texto utilizando pytesseract
texto = pytesseract.image_to_string(r'imagen.jpg', lang=idioma_origen)

# Traduce el texto utilizando googletrans
traductor = translator()
traduccion = traductor.translate(texto, src=idioma_origen, dest=idioma_destino)

# Guarda el texto original y la traducción en un archivo de texto plano
with open('resultado.txt', 'w') as file:
    file.write(f'Texto original ({idioma_origen}): {texto}\n')
    file.write(f'Traducción ({idioma_destino}): {traduccion.text}\n')
