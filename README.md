# World-Cup-Russia-2018-Simulator
Final project for the subject Operative Systems in UCLA Venezuela

Guía de instalación
Dado que un requisito del programa es que sea desarrollado en Python para Linux, **se asume que el usuario cuenta con una distribución 
GNU/Linux con el lenguaje Python en una versión 3.x**. En nuestro caso trabajamos con Debian 8.10 Jessie y Kubuntu 18.04, usando Python 
3.6.5. 

Lo primero es abrir una terminal para ejecutar los comandos. El programa usa la librería blessings, por lo que es necesario descargarla, 
para esto, primero instalamos pip ejecutando el siguiente comando:

  `sudo apt-get install python3-pip`

Luego procedemos a instalar la librería requerida usando el siguiente comando:

  `pip3 install blessings`

Una vez esté instalado debemos descargar el proyecto.

Luego, en la terminal, debemos dirigirnos hacia el directorio donde descargamos el archivo, para esto usamos el siguiente comando:

  `cd ruta-del-directorio`

**Reemplazando por la ruta respectiva**, por ejemplo, en mi caso: `home/pythonprojects/wc2018simulator`

Ahora ya está todo listo para ejecutar el programa, solo debemos ejecutar el siguiente comando en la terminal:

  `Python3 main.py`

Y listo, el programa se ejecutará en la consola y podrás obtener un pronóstico de quién será el campeón de la copa mundial, debe presionar 
la tecla **ENTER** para avanzar entre rondas.

Recordamos que pueden editar el archivo configuración.py para cambiar las probabilidades de los equipos, así como la velocidad de ejecución 
si desean vivir la simulación en tiempo más real. 
