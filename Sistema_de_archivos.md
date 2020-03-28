# Sistema de archivos

Utilizamos la herramienta ``ampy`` que puede ser instalada desde la consola usando el siguiente comando

(Es necesario tener ``python3`` con el PATH agregado):
    
    pip3 install adafruit-ampy

La documentación completa pueden encontrarla en GitHub

    https://github.com/pycampers/ampy

Antes de usar ``ampy`` es importante cerrar todas las sesiones activas en la que se use el puerto serial del dispositivo que vamos a usar, ya sea ``ESPlorer, PuTTY, jupiter``.

ampy - Herramienta Adafruit MicroPython

   Ampy es una herramienta para controlar placas MicroPython a través de una conexión en serie.
   Usando ampy puedes manipular archivos en el sistema de archivos interno de la placa y
   incluso ejecutar scripts.

### Comandos básicos

Uso: ampy [OPCIONES] COMANDO [ARGS] ...

Opciones:
   -p, --port PORT Nombre del puerto serie para la placa conectada. [necesario]
   -b, --baud BAUD Velocidad en baudios para la conexión en serie. (predeterminado 115200)
   -d, --delay DELAY Retraso en segundos antes de ingresar al MODO RAW (valor predeterminado 0)
   --help Imprime información en consola sobre el uso de la herramienta

Comandos | Acción
--- | ---
get | Extraer un archivo de la ``placa Smart Home``.
ls | Lista el contenido de un directorio en la ``placa Smart Home``.
poner | Poner un archivo en la ``placa Smart Home``.
rm | Eliminar un archivo de la ``placa Smart Home``.
run | Ejecuta un script en la ``placa Smart Home`` e imprime su salida.

### Ejemplos de uso 

1 Listar archivos

    ampy -pCOMxx ls

2 Subir un archivo

    ampy -pCOMxx put BMEM280.py    

3 Subir un archivo y guardarlo con otro nombre

    ampy -pCOMxx put archivo.py main.py

4 Correr un archivo

    ampy -pCOMxx run archivo.py

4 Eliminar un archivo

    ampy -pCOMxx rm archivo.py

5 Copiar un archivo del ESPxx a nuestro ordenador

    ampy -pCOMxx get archivo.py    
    

6 Crear una carpeta

    ampy -pCOMxx mkdir carpeta_X

7 Eliminar una carpeta

    ampy -pCOMxx rmdir carpeta_x