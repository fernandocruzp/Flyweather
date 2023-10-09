# Flyweather
##Integrantes:
*Cruz Pineda Fernando
*Marquéz Corona Danna Lizette
*Flores Carrillo Itzel Paola
*Espinosa Roque Rebeca
## Tabla de Contenidos
1. [Definición del Problema](#definición-del-problema)
2. [Análisis del Problema](#análisis-del-problema)
3. [Mejor Alternativa](#mejor-alternativa)
4. [Herramientas utilizadas](#herramientas-utilizadas)
5. [Ejecución](#ejecución)

## Definición del Problema
***
El problema consiste en desarrollar una aplicación de software que proporcione información actualizada sobre el clima 
de dos ciudades, la ciudad de salida y la ciudad de llegada, para vuelos que salen el mismo día en que se ejecuta el 
algoritmo. La interfaz debe ser interactiva, intuitiva y amigable ya que está dirigida a usuarios que  no tienen 
conocimientos de programación.
#### Requisitos Funcionales
* La aplicación acepta como entrada un ticket o el nombre de la ciudad de la que se desea conocer el clima.
* La entrada es flexible para manejar errores tipográficos y diferentes formas de escribir el nombre de la ciudad.
* Muestra el informe del clima de la ciudad de salida y la ciudad de llegada en un formato fácil de entender.
* Es capaz de manejar posibles errores en las consultas al servicio web y proporcionar retroalimentación al usuario en caso de problemas.
#### Requisitos No Funcionales
* La aplicación es interactiva, intuitiva y amigable para usuarios sin conocimientos de programación.
* Se deben realizaron pruebas exhaustivas para asegurar la funcionalidad y la calidad del software.
* El proyecto es estético y funcional.

## Análisis del Problema
***
##### Datos proporcionados
Se cuentan con dos archivos (dataset1.cv y dataset2.csv) los cuales contienen los IATA codes de las ciudades de las que 
quiere obtener la información climática, además de que el segundo archivo proporciona el número de ticket, estos 
archivos incluyen además el coordenadas geográficas de las ciudades. 
#### Datos de Salida
Se obtienen datos como la temperatura, humedad, presión de un lugar específico, lo cual responde las demandas que 
se han echo.
#### ¿Qué se necesita?
Se necesita acceder a los datos del clima de una ciudad en específico, dado su código IATA o los datos de su latitud y
longitud, esto nos permitirá hacer peticiones a alguna API especializada en esta área, que nos regresará los datos 
necesarios para completar lo que se nos solicita. Además de que la aplicación deberá de recibir dos opciones de entrada, 
así como ser robusto a errores de escritura.

## Mejor Alternativa 
***
Para resolver la parte de la obtención del clima, se usrá alguna API meteorológica, sin embargo, como se 
usará alguna versión gratis esto nos forzará a utilizar un caché para almacenar el clima de las ciudades que se vayan
buscando y de esta manera no hacer peticiones a la API que ya se han hecho previamente. 

:) 

Para solucionar la demanda de que el programa sea robusto a que se proporcione el nombre de la ciudad, y no el código 
IATA, así como la incorrecta escritura de este, se usará un algoritmo para encontrar la compatibilidad(?) entre dos 
string, así como relacionar el nombre de la ciudad con su código IATA.

## Herramientas utilizadas
***
 * **OpenWeatherMap** - Se seleccionó usar OpenWeatherMap por la sencillez de su uso, además de que la versión gratis 
    cumple completamente con los propósitos para los que se requiere.
 * **FLASK** - Utilizamos la paquetería flask como framework para realizar nuestra página web ya que este nos permite crear
   aplicaciones web de manera rapida y con un minimo número de lineas de codigo.
 * **requests** - Para realizar la llamada a la API 
 * **thefuzz** - para solucionar el problema de los mispelled names se usará la función *extractOne()* de la paquetería
   thefuzz, la cual usa Levenshtein para encontrar de una lista de strings a aquella cadena que tiene mayor coincidencia
   con el string dado.
 * **GitHub** - al ser la primera vez creando pruebas unitarias en Python, se ha revisado varios repositorios en GitHub
                para darse una idea de cómo realizarlas, en especial se ha tomado en cuenta al usuario
                 [DiegoPartida13](https://github.com/DiegoPartida13) del archivo *Proyecto1/Proyecto01/test/test_Ayuda_API.py*
                

## Ejecución
***
Requisitos previos.
+python3
+instalación de las siguientes paqueterías de python:
    *Flask
      $ pip install Flask
    *thefuzz
      $ pip install thefuzz
    *requests
      $ pýthon -m pip install requests
En la raiz del proyecto ./FlyWeather escriba el comando python main.py
Con esto se iniciará el servidor de flask, una vez se allá iniciado, en su navegador web ingrese a http://127.0.0.1:5000/

Para ejecución de de las pruebas unitarias:
En la raiz del proyecto ./FlyWeather escriba el comando 
$ python Test/Test.py python 
$ Test/test_Buscador.py 
$ python Test/test_LlamaAPi.py 

