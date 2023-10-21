from gpiozero import LED
import time

# Configura los LEDs en los pines GPIO 17, 18, 22 y 23
leds = [LED(17), LED(18), LED(22), LED(23)]

# Función para encender los LEDs según la secuencia del archivo
def encender_leds(secuencia):
    for i, estado in enumerate(secuencia):
        if estado == '1':
            leds[i].on()
        elif estado == '0':
            leds[i].off()

# Lee el archivo de texto
def leer_archivo():
    with open("secuencia.txt", "r") as archivo:
        return archivo.readline().strip()

while True:
    # Lee la secuencia del archivo
    secuencia = leer_archivo()

    # Verifica si la secuencia es válida
    if len(secuencia) == len(leds):
        encender_leds(secuencia)
    else:
        print("La secuencia no tiene la cantidad correcta de elementos.")

    time.sleep(1)
