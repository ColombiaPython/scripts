# Scripts para ColombiaPython

Una colección de _scripts_ para realizar diferentes tareas de procesamiento
relacionadas con ColombiaPython.

## pycon-metricas

Esta carpeta contiene scripts para el procesamiento de datos relacionados
con PyCon Colombia 2018. Actualmente contiene scripts para la generación 
de nubes de palabras (_wordclouds_) a partir de los _tweets_ asociados al
evento.

## Dependencias

Los scripts pueden ser ejecutados en los dialectos 2 y 3 de Python
y requieren de los siguientes paquetes:

- ``beautifulsoup4``.
- ``wordcloud``.

### Web scrapping
El script ``pycon_tweets_scrapping.py`` genera un archivo de texto plano
a partir de un conjunto de tweets. En nuestro caso, se usó un archivo
html con esta información que no se incluye por razones de derechos de
autor. Para ejecutar este script

    python pycon_tweets_scrapping.py


### Generación de la nube de palabras

El script ``pycon_tweets_scrapping.py`` genera una imagen a partir de:

- **Texto plano:** del cual se obtienen las palabras.
- **Stopwords:** que define las palabras que no se incluirán en la
  visualización.
- **Máscara:** imagen en blanco y negro con la silueta para la nube
  de palabras.

