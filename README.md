# World-Cup-Russia-2018-Simulator
Final project for the subject Operative Systems in UCLA Venezuela.
Proyecto final de la asignatura Sistemas Operativos en la UCLA Venezuela.

**Installation guide**
A requirement for the program is that it must be developed using Python in Linux, hence **It is assumed the user has a
GNU/Linux with Python language version 3.x. The following instructions ar intended for Ubuntu**.

**Guía de instalación**
Dado que un requisito del programa es que sea desarrollado en Python para Linux, **se asume que el usuario cuenta con una distribución GNU/Linux con el lenguaje Python en una versión 3.x. Las siguientes instrucciones son van dirigidas a la distribución Ubuntu.**

1) First step is to open a terminal for running the commands. The program uses the *blessings* library, so we must install it,
for this, first install pip running the following command:

1)Lo primero es abrir una terminal para ejecutar los comandos. El programa usa la librería *blessings*, por lo que es necesario descargarla, para esto, primero instalamos pip ejecutando el siguiente comando:

  `sudo apt-get install python3-pip`

2)Then we install the required library using the next command:

2)Luego procedemos a instalar la librería requerida usando el siguiente comando:

  `pip3 install blessings`

3)Once it is installed we must download the project. After that, in the terminal, we must go to the directory where the
project is downloaded, for this we use the next command:

3)Una vez esté instalado debemos descargar el proyecto. Luego, en la terminal, debemos dirigirnos hacia el directorio donde descargamos el archivo, para esto usamos el siguiente comando:

  `cd ruta-del-directorio`

**Replacing for your own route.**, in my case: `home/pythonprojects/wc2018simulator`
**Reemplazando por la ruta respectiva**, por ejemplo, en mi caso: `home/pythonprojects/wc2018simulator`

4)Now it is ready for running,  just run the next command in the terminal:

4)Ahora ya está todo listo para ejecutar el programa, solo debemos ejecutar el siguiente comando en la terminal:

  `Python3 main.py`

And it is done,  the program will ru and you could get a forecast of the world cup champion. Press the **RETURN** key to 
advance between rounds.

Y listo, el programa se ejecutará en la consola y podrás obtener un pronóstico de quién será el campeón de la copa mundial, debe presionar la tecla **ENTER** para avanzar entre rondas.


You can edit configuracion.py for changing the teams probabilities and the rurunning speed.

Pueden editar el archivo configuración.py para cambiar las probabilidades de los equipos, así como la velocidad de ejecución 
si desean vivir la simulación en tiempo más real. 

PD: This program uses libraries only available for Linux, Windows OS are not supported. 
PD: Este programa usa librerías disponibles solo para Linux, Windows OS no son soportados. 
