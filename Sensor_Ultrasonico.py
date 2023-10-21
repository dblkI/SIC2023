import RPi.GPIO as GPIO
import time
import datetime

# Configuración de pines GPIO
TRIG = 23  # Pin del sensor de ultrasonido TRIG
ECHO = 24  # Pin del sensor de ultrasonido ECHO
RED_LED = 17  # Pin del LED rojo
AMBER_LED = 27  # Pin del LED ámbar
GREEN_LED = 22  # Pin del LED verde

# Configuración de pines GPIO como salida o entrada
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(AMBER_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)

def distancia_ultrasonico():
    # Generar pulso de ultrasonido
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    inicio_tiempo = time.time()
    fin_tiempo = time.time()

    # Esperar a que el ECHO se active
    while GPIO.input(ECHO) == 0:
        inicio_tiempo = time.time()

    # Esperar a que el ECHO se desactive
    while GPIO.input(ECHO) == 1:
        fin_tiempo = time.time()

    # Calcular la distancia en centímetros
    duracion = fin_tiempo - inicio_tiempo
    distancia = (duracion * 34300) / 2

    return distancia

try:
    while True:
        distancia = distancia_ultrasonico()
        fecha_actual = datetime.datetime.now()
        mensaje_alerta = ""

        if distancia < 10:
            GPIO.output(RED_LED, GPIO.HIGH)
            mensaje_alerta = "MUY CERCA"
        elif distancia > 30:
            GPIO.output(GREEN_LED, GPIO.HIGH)
            mensaje_alerta = "EXCELENTE"
        else:
            GPIO.output(AMBER_LED, GPIO.HIGH)
            mensaje_alerta = "CERCA"

        # Guardar la información en un archivo .txt
        with open("mediciones.txt", "a") as archivo:
            archivo.write(f"Distancia: {distancia} cm, Alerta: {mensaje_alerta}, Fecha: {fecha_actual}\n")

        # Esperar un segundo antes de tomar otra medición
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
