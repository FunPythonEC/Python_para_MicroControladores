# Empezando con micropython en ESP32 version Windows

## Instalar herramientas

1 Instalar Java

    https://www.java.com/es/download/

2 Descargar ESPLORER y descomprimir

    http://esp8266.ru/esplorer-latest/?f=ESPlorer.zip

Sera el IDE para programar el esp32 con micropython

3 Instalar python cualquier version, y marcar la casilla agregar al PATH durante la instalacion

    https://www.python.org/downloads/windows/

4 Instalar ESPTOoL

    pip install esptool

para mas info :
https://github.com/espressif/esptool/

5 Instalar ampy 

    pip install adafruit-ampy

para mas info:
https://github.com/pycampers/ampy

## Cargar "flashear" el firmware en el ESP32

1 Descargar el firmware micropython especificamente :

    https://micropython.org/resources/firmware/esp32-20190529-v1.11.bin

Para ver mas versiones visitar https://micropython.org/download#esp32

2 Conectar el USB y en administrador de dispositivos verificar el numero de puerto COM 

9 Abrir la terminal y con el sig comando borrar el flash del esp32

    esptool --chip esp32 erase_flash

8 Luego grabar el binario que descargarmos en el ESP32

Cambiar el numero del puerto COM

al final ponemos la direccion de nuestro binario

    esptool --chip esp32 --port COM8 --baud 460800 write_flash -z 0x1000 C:\Users\Descargas\esp32-20190529-v1.11.bin

## Probando MicroPython

1 Abrimos el ejecutable EspLorer.py

2 En la pestaña SETTINGS marcar la casilla "micropyhon"

3 Damos clic en OPEN para abrir el puerto y 

4 Doble clic en RST para resetear el chip o podemos pulsar el boton de la plaza y veremos micropython en nuestra consola
