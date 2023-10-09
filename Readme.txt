Instrucciones de Configuración y Ejecución de FlyWeather
23 de septiembre de 2023

1. Requisitos Previos
Antes de comenzar con FlyWeather, asegúrate de que tu entorno cumpla con
los siguientes requisitos:
Python 3.7 o mayor instalado.
Las siguientes paqueterı́as de Python instaladas:
• Flask :  Utilizamos la paquetería flask como framework para realizar nuestra página web ya que este nos permite crear aplicaciones web de manera rapida y con un minimo número de lineas de codigo.
Instalación:
	$ pip install -U Flask
• thefuzz: Para solucionar el problema de los mispelled names se usará la función extractOne() de la paquetería thefuzz, la cual usa Levenshtein para encontrar de una lista de strings a aquella cadena que tiene mayor coincidencia con el string dado.
Instalación:
	$ pip install thefuzz
• requests:  Para realizar la llamada a la API
Instalación:
	$ python -m pip install requests
2. Configuración y Ejecución
Sigue estos pasos para configurar y ejecutar FlyWeather:
1. Coloca todo el contenido del proyecto FlyWeather en la raı́z de tu direc-
torio de trabajo, clonando el repositorio con $ git clone https://github.com/fernandocruzp/Flyweather.git.
2. Abre una terminal en la raı́z del proyecto, donde se encuentra el archivo
main.py.
3. Ejecuta el siguiente comando para iniciar el servidor de Flask:
python main . py
4. Una vez que el servidor Flask se haya iniciado con éxito, abre tu navegador
web y accede a la siguiente dirección: http://127.0.0.1:5000/

3. Ejecución de Pruebas Unitarias
Para ejecutar las pruebas unitarias de FlyWeather, sigue estos pasos:
1. Abre una terminal en la raı́z del proyecto, donde se encuentra el archivo
Test.py.
2. Ejecuta el siguiente comando para ejecutar las pruebas generales:
python Test / Test . py
3. Ejecuta el siguiente comando para ejecutar las pruebas del buscador:
python Test / t e s t B u s c a d o r . py
4. Ejecuta el siguiente comando para ejecutar las pruebas de la llamada a la
API:
python Test / test LlamaAPI . py
¡Ahora estás listo para configurar, ejecutar y probar FlyWeather!



**Integrantes:

    Cruz Pineda Fernando
    Marquéz Corona Danna Lizette
    Flores Carrillo Itzel Paola
    Espinosa Roque Rebeca
