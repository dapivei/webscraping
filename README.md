# Scrapping

***

<div align="justify">

<image width="50" height="50" src="./images/warning_sign.png"> **Advertencia:** Para ejecutar los *scripts* asociados al presente repositorio, asegúrese de tener todas las paqueterías especificadas en el documento [requirements.txt](https://github.com/dapivei/webscraping/blob/master/requirements.txt). Si no las tiene instaladas, ejecutar la línea de comandos la instalación de las mismas, de la siguiente manera:

```
pip3 install <paquetería>
```

El presente repositorio contiene **scripts** que permiten realizar las siguientes tareas:

**1.** Scraping de todas las noticias publicadas en https://www.eldiario.net, con el fin de obtener información relacionada con el autor, la fecha de publicación, el lugar, etc., para un periodo de tiempo fijado. El tiempo para el scrapeo se fijó en dos días anteriores a la fecha de scrapeo, pero esto puede ser fácilmente adecuado al gusto del usuario, modificando la variable "days_ago" del documento [main_scraping](https://github.com/dapivei/webscraping/blob/master/main_scraping.py). *Nota:* El código podría fácilmente adecuarse para el scrapeo de otras páginas.

El *script* principal, que orquesta todas las operaciones necesarias para realizar el scrapeo, es el documento [main_scraping.py](https://github.com/dapivei/webscraping/blob/master/main_scraping.py), mismo que se apoya en otros dos scripts que contienen funciones auxiliares: [auxiliar_functions.py](https://github.com/dapivei/webscraping/blob/master/auxilar_functions.py) y [functions_pagina_siete.py](https://github.com/dapivei/webscraping/blob/master/functions_pagina_siete.py).

Para correr el código, situarse sobre la línea de comandos y ejecutar el siguiente código:

```
git clone https://github.com/dapivei/webscraping
```
En la línea de comandos situarse sobre la carpeta webscraping

```

cd <<path donde se ubica la carpeta webscraping>>

```

Ejecutar:

```
python3 main_scraping.py
```


Revisar en la carpeta *webscraping* el output: un excel denominado `paginasiete.csv`.


*Documentos adicionales:* Además de los documentos mencionados, en el documento [selenium_newspaper_scraper.ipynb](https://github.com/dapivei/webscraping/blob/master/selenium_newspaper_scraper.ipynb), puede encontrar el notebook asociado a los tres documentos antes mencionados, juntos con los outputs esperados. También, puede remitirse al documento [beautifulsoup_newspaper_scraper.ipynb](https://github.com/dapivei/webscraping/blob/master/beautifulsoup_newspaper_scraper.ipynb), documento en el cuál se implementó un scrapeo de la página principal de https://www.eldiario.net, empleando la paquetería `beautifulsoup4`.

**2.** Código que permite recoger los tweets (mediante un scraper) de la cuenta de Nelson Peredo (@nperedo). Idealmente quisierámos recoger los tweets de los últimos 7 días; sin embargo, para realizar tal tarea se necesita una cuenta de developper en [Tweepy](https://www.tweepy.org,). Al momento de la realización del presente ejercicio, solicité los permisos necesarios en Tweepy, sin embargo, mi trámite aún está en proceso. Por lo anterior, realicé este ejercicio con otra librería: GetOldTweets, misma que te da todos los tweets del usuario de interés, excepto aquellos correspondienres al mes más reciente. El código asociado se encuentra en el *script* [tweet_scraper.py](https://github.com/dapivei/webscraping/blob/master/tweet_scraper.py).

Para ejecutarlo, habiendo clonado previamente el repositorio y estando situando sobre la carpeta webscraping:

```
python3 tweet_scraper.py
```
Revisar en la carpeta *webscraping* el output: un excel denominado `tweet_search.csv`.

*Documentos adicionales:* Además de los documentos mencionados, en el notebook [twitter.ipynb](https://github.com/dapivei/webscraping/blob/master/twitter.ipynb), puede seguir la ejecución del código paso a paso, junto con los resultados esperados.
