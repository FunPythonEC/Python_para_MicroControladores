## Existen dos formas de cargar librerias externas de micropython en el ESPXX
## Forma 1
Descargandola desde internet manualmente o creando tu propia libreria. Y grabarla en el esp32 utilizando ampy(la guia se ``llama sistema de archivos``)

Utilizando el comando para cargar el script.py

    ampy -pCOMxx put max7219.py

Esperamos unos segundos, un truco es presionar las teclas ``ctrl +  c`` y ejecutar el comando anterior de nuevo

Para verificar podemos listar los archivos de nuestro ESPxx con le siguiente comando:

    ampy -pCOMxx ls

## Forma 2

Al igual que en ``python`` contamos con ``pip`` en ``micropython`` tenemos ``upip``

Para usarlo tenemos que conectarnos a internet primero, asi que usamos el ejemplo **conectarse_a_wifi.py** del repositorio
cambiamos el nombre de la red y la contraseña de ser necesario y procedemos a enviar el script utilizando el **boton Send to ESP** y en unos segundos veremos que se conecta a la red e imprime la ip 

luego en otro archivo o pestaña del ESPlorer escribimos las siguientes lineas

```python
import upip
micropython -m upip install micropython-pystone


# Se imprimira en la consola serial que esta descargando e instalando la libreria

>>> import pystone
>>> pystone.main()
Pystone(1.2) time for 50000 passes = 0.534
This machine benchmarks at 93633 pystones/second
```

Puedes enviar tambien
micropython -m upip --help para mas informacion o revisar la documentacion del siguiente link

    https://github.com/pfalcon/pycopy-lib

https://pypi.org/project/micropython-upip/https://github.com/pfalcon/pycopy-lib