from gpiozero import Button
from datetime import datetime
from time import sleep

# Configura el botón en el pin GPIO 17
boton = Button(17)

# Función para escribir la fecha y hora en un archivo
def escribir_fecha_hora():
    now = datetime.now()
    fecha_hora = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("registro_botones.txt", "a") as archivo:
        archivo.write(f"Botón presionado en: {fecha_hora}\n")

# Espera a que se presione el botón y luego escribe la fecha y hora
while True:
    boton.wait_for_press()
    escribir_fecha_hora()
    sleep(1)  # Espera 1 segundo para evitar múltiples detecciones con un solo clic