# <h1 align=center><span style="color:blue"> **Training Project about Data Engineering** </span></h1>

<p align="center">
<img src="https://camo.githubusercontent.com/09bd9c8fd059de237050145eff2d484627bf3ffe6958205914d3af018357e998/68747470733a2f2f66696c65732e7265616c707974686f6e2e636f6d2f6d656469612f576861742d69732d446174612d456e67696e656572696e675f57617465726d61726b65642e3630376537363161336330652e6a7067"  height=300>
</p>

## **Introducción**
<p>Me propuse realizar un pipeline de tratamiento de datos que incluye, extracción de datos, creación de una API web, y deployment de esta en un sitio web. Para comenzar, nuestro insumo estaba formado por cuatro datasets, que contenían los datos de cuatro reconocidas plataformas de servicio de video on-demand(Amazon Prime, Disney, Hulu y Netflix). En segundo lugar, el tratamiento de datos, consistió en una pequeña transformación a pedido del cliente, debido a que le interesaba que los datos nulos no fuesen modificados, excepto aquellos en uno solo de los campos. Para esto utilizamos Python y algunas dependencias especializadas en el tratamiento de datos. En tercer lugar, la creación de la API fue llevada adelante utilizando el framework fastapi y Python como lenguaje de programación. Para finalizar, realizamos el deployment utilizando el sitio web de Render.
    
</p>
<hr>  
<p align="center">
  <img src="https://umd-today.files.svdcdn.com/production/hero/streaming_animated_1920x1080.gif" alt="GIF" width="1000" height="500" />
</p>
<hr>  

## **Desarrollo del proyecto**

### **ETL**

En  principio, contábamos con cuatro datasets de distintas plataformas de entretenimiento(Amazon Prime, Disney, Hulu y Netflix). Todos los  datasets estaban en formato csv.

<p>En primer lugar, realizamos el proceso de ETL con Jupyter Notebooks ( archivo ETL.ipynb). Optamos por cargar los cuatro datasets y realizar el proceso simultáneamente, en lugar de realizar todos los pasos para un dataset y luego comenzar con el siguiente. 
La transformación debió cumplir con los siguientes requisitos:

- "Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)"

- "Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”"

- "De haber fechas, deberán tener el formato AAAA-mm-dd"

- "Los campos de texto deberán estar en minúsculas, sin excepciones"

- "El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)" 
<p/>
<p>
Para cumplir con los requisitos planteados solo fueron necesarios las librerías Pandas y Numpy. Además Pandas no solo fue utilizado para la transformación de datos, sino también para su carga y almacenamiento.
</p>


### **Creación de la API**
<p>
El objetivo de este paso era realizar cinco queries desde una web API.
Para cumplir con este punto se escogió FASTAPI.
</p>
La creación de la API consta un solo archivo .py, a saber main.py y algunos archivos .ipynb para trabajar el proyecto como un solo paquete. Debido a que no se utilizó una base de datos, no fue necesario crear archivos para el manejo de esta, ni para los modelos de algún ORM que mapeara las tablas relacionales, ni tampoco para los clásicos schemas de PYDANTIC. Las librerías utilizadas
en el script main.py fueron, fastapi, pandas y uvicorn. 

Aclaramos que por una cuestión práctica, todas las funciones fueron nombradas igual que la consulta que llevan adelante. Aunque en un caso real, por cuestiones de seguridad, esta práctica no está aconsejada.

Las consultas a que realiza esta API son:

**1) Cantidad de veces que aparece una substring en el título de peliculas/series, por plataforma:
    El request debe ser: get_word_count(keyword, plataforma)**

Para esta query se creó la función `get_word_count(keyword: str, nombreDePlataforma: str)` que recibe la palabra que queremos buscar en los títulos y el nombre de la plataforma, además retorna una string con la información solicitada. 


**2) Cantidad de películas por plataforma que superen a un puntaje dado en un determinado año**
    
Esta query se realiza gracias a la función `get_score_count(nombreDePlataforma: str, score: int, year: int)` . Esta recibe como parámetro una string (el nombre  de la plataforma), el puntaje(int) y el año(int), luego retorna una string.



**3) La segunda película con mayor score para una plataforma determinada, según     el orden alfabético de los títulos.
    El request debe ser: get_second_score(nombreDePlataforma):**
    
La función encargada de llevar a cabo esta query es `get_second_score(nombreDePlataforma: str)` que recibe una string(nombre de la plataforma) como parámetro y devuelve otra string que tiene el mayor puntaje de la plataforma y que, además, se encuentra segunda en orden alfabético entre todas las películas con mayor puntaje.
    
**4) Película que más duró según año, plataforma y tipo de duración 
    El request es: get_longest(plataforma, medida, year)**
  
 Esta query fue abordada con la función `get_longest(plataforma: str, medida: int, year: int)` que recibe dos strings, plataforma y medida, la primera con el nombre de la plataforma. La segunda, contiene la unidad de medida de la duración de la película. El tercer parámetro es un int, el año solicitado. Esta función retorna una string.
    
**5) Cantidad de películas y series por rating.
    get_rating_count(rating)**
    
Esta query es resuelta por la función `get_rating_count(rating: str)` que recibe una string con el tipo de calificación por edades de la película y retorna una string informando el total de películas con este rating en las cuatro plataformas como conjunto. 


### **Deployment**

Para la última fase de nuestro pipeline, elegimos Render que es un servicio web que permite construir y almacenar aplicaciones web en la nube. En este paso seguimos las instrucciones de la documentación de fastapi. La dirección web de nuestra api se encuentra en https://data-engineering-mauro.onrender.com/docs .
## **Puntos a mejorar en este proyecto**

Los siguientes son algunos puntos que podrían enriquecer el proyecto:

1) Crear un subdirectorio adicional que contenga al script main y a todos los datasets procesados, de manera de mejorar la organización. 

2) Mejorar las restricciones de los inputs de FASTAPI, en la quinta función

3) Realizar un EDA-ETL en profundidad, dado que no formaba parte de los requisitos del proyecto.

4) Quitar la función de testeo `read_root(nombre)`

<hr>
<p align="center">
  <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaG9xOHZ0b3Y4bGZnemx5dDZxajVqeDI2MGRla2ZoaWppaTNqbWExeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4uMy0wqz6V1SM/giphy.gif" alt="GIF" width="600" height="300" />
</p>
<hr>

## Sitios con información sobre este proyecto

**`Deployment de la api`**
- https://data-engineering-mauro.onrender.com/docs

**`Repositorio Github`**

- https://github.com/Superior-Mauro/Project_Data_Engineering
