Rafael Zermeño Cervantes – Sprint 8
(QA14)

Para este proyecto utilizamos Pyton, Pycharm, Git(gitbash) y GitHub, sigue los pasos a continuación.
-	Intérprete de Python: Entrar a la página oficial en descargas y dar clic al botón amarillo (detecta automáticamente tu sistema operativo). Descargar e instalar
https://www.python.org/downloads/
-	.Descarga Pycharm (Edición comunitaria de PyCharm)
https://www.jetbrains.com/pycharm/download/?section=windows
-	Descarga Git:
https://git-scm.com/downloads
-	Crea una cuenta en GitHub:
https://github.com/


Es necesario instalar el siguiente controlador para google chrome:
El controlador o driver para google Chrome última versión y de acuerdo a nuestro sistema operativo. Podemos encontrar el que corresponda con nuestro sistema mediante el siguiente enlace:

https://googlechromelabs.github.io/chrome-for-testing/#stable

Una vez descargado, crearemos una carpeta llamada “WebDriver” y dentro ella otra carpeta llamada “bin”. Donde guardaremos nuestro driver
Esta es mi ruta:

C:\WebDriver\bin


Una vez instalado es necesario hacer unas configuraciones en Windows para evitar conflictos con Python y el resto de los programas que necesitaremos:
 
1.- Ubicar el archivo de instalación del intérprete de Python y obtener la ruta. En mi caso es:
-	C:\Users\Spartan83\AppData\Local\Programs\Python\Python312
2.- De igual manera ubicar las siguientes carpetas: Scripts y site-packages y obtener las rutas:
-	C:\Users\Spartan83\AppData\Local\Programs\Python\Python312\Scripts
-	C:\Users\Spartan83\AppData\Local\Programs\Python\Python312\Lib\site-packages
3.- También obtén la ruta del driver de googlechrome.
-	C:\WebDriver\bin

4.- ir a configuración avanzada del sistema > Opciones avanzadas > variables de entorno
-	En variables de usuario seleccionar "Path" y dar clic en Editar. 
-	Dar clic en "nuevo" y añadir uno a uno las rutas.
NOTA: Posicionar las 3 rutas en las primeras 3 posiciones con el botón subir, para evitar conflictos con otros programas. Todo esto es con la finalidad de poder instalar las librerías, pytest, pip, selenium etc. para llevar a cabo las instalaciones necesarias en los programas que ocuparemos en nuestro proyecto.
__________________________________________________________________

Abrimos Pycharm e instalamos las librerías de la siguiente manera:
En la parte inferior se encuentra la consola de Python. Hay dos formas de instalar. La más fácil es ir a icono que “Python packages” y en la barra de búsqueda teclear:
-	Pip y elegir la última versión e instalar.
-	Pytest, y elegir la última versión e instalar.
-	Request e instalar (esta es nuestra librería) 
-	Selenium y elegir la última versión e instalar.


Otra manera es teclear en la terminal:
•	pip install pytest
•	pip install requests
•	pip selenium


OBJETIVO DEL PROYECTO:
El proyecto consta de llevar a cabo una serie de pruebas automatizadas usando Google Chrome, en la página web llamada: UrbanRoutes. Que nos sirve para solicitar un taxi o rentar un automóvil personalizado. Pero para este Test solo nos concentraremos en solicitar propiamente un taxi de la tarifa confort.
Para ello realizaremos pruebas en elementos de la página tales como:
-	Función de botones de tres tipos (normal, deslizable, botón contador).
-	Llenado de campos como: teléfono, código sms, tarjeta, código de tarjeta, enviar un mensaje al conductor).
Para ello necesitamos trabajar con tres archivos donde obtendremos nuestras solicitudes a la hora de automatizar las pruebas:

Para llevar a cabo los casos de prueba para el proyecto, trabajaremos con este archivo en PyCharm: 
                                      “qa-project-Urban-Routes-es”
Para obtenerlo necesitaremos con la ayuda de GitBash hacer una clonación del archivo.
Entraremos a GitHub y colcaremos la ruta donde clonaremos nuestro archivo. en mi caso quedaría asi:
Cd “C:\Users\Spartan83\projects”
Escribiremos lo siguiente:
-	git clone https://github.com/usuario/qa-project-Urban-Routes-es.git
En mi caso queda asi:
-	git clone https://github.com/RafaelZeCe83/qa-project-Urban-Routes-es.git
Y quedara guardado de la siguiente manera:
C:\Users\Spartan83\projects\qa-project-Urban-Routes-es
En el proyecto se encuentran los siguientes archivos:
-	.gitignore
-	README.md
-	Data.py
-	Main.py
Pero, por buenas prácticas se nos recomendó dividir las herramientas a utilizar en archivos independientes, tales como:
-	my_locators.py
-	my_methods.py
Teniente en total 6 archivos:
-	.gitignore
-	README.md – (descripción del proyecto Sp8)
-	Data.py – (URL, y demás variables con información a introducir en campos correspondientes)
-	my_locators.py – (Aquí se encuentran nuestros localizadores que emplearemos en nuestros métodos. Los cuales leindicamos a Pycharm y Selenium la ubicación más exacta posible para realizar los métodos.
-	my_methods.py – (Aquí se encuentra nuestro códigos y métodos que empleamos tales como: esperas, clicks, llenado de campos, uso de gets para obtener texto, atributos, etc que nos ayudaran en nuestros test)
-	Main.py – Aquí propiamente llevaremos a cabo nuestras pruebas)



EJERCICIOS A REALIZAR:
Escribe pruebas automatizadas que cubran el proceso completo de pedir un taxi. Las pruebas deben cubrir estas acciones:

1.	Configurar la dirección (esta parte se ha escrito para ti como ejemplo).
2.	Seleccionar la tarifa Comfort.
3.	Rellenar el número de teléfono.
4.	Agregar una tarjeta de crédito. (Consejo: el botón 'link' (enlace) no se activa hasta que el campo CVV de la tarjeta en el modal 'Agregar una tarjeta', id="code" class="card-input", pierde el enfoque. Para cambiar el enfoque, puedes simular que el usuario o usuaria presiona TAB o hace clic en otro lugar de la pantalla).
El repositorio tiene preparada la función retrieve_phone_code() que intercepta el código de confirmación requerido para agregar una tarjeta.

5.	Escribir un mensaje para el controlador.
6.	Pedir una manta y pañuelos.
7.	Pedir 2 helados.
8.	Aparece el modal para buscar un taxi.
9.	Esperar a que aparezca la información del conductor en el modal (opcional). Además de los pasos anteriores, hay un paso opcional que puedes comprobar; este es un poco más complicado que los demás, pero es una buena práctica, ya que es probable que en tu trayectoria profesional encuentres tareas más difíciles.



Para ejecutar las pruebas hay que hacer lo siguiente.

-	Actualizar la URL en data.py para poder correr las pruebas, de lo contrario no podremos arrancar las pruebas.
-	Hay que configurar la ejecución de la prueba:
•	Ir a Run > Edit Configurations.
•	Haz clic en el botón "+" y selecciona "Python tests" y luego "pytest".
•	Configura el nombre y el directorio o archivo de prueba que deseas ejecutar, y haz clic en "OK".


Ahora ponemos ejecutar esta configuración desde el menú desplegable en la esquina superior derecha.

Otra manera es desde la terminal escribiendo:
Pytest y enseguida el nombre de nuestro archivo

Ej:

pytest main.py







