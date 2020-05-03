# Scrapping

***

<div align="justify">

El presente repositorio contiene *scripts* que permiten realizar las siguientes tareas:

**1.** Scraping de todas las noticias publicadas en https://www.eldiario.net, con el fin de obtener información relacionada con el autor, la fecha de publicación, el lugar, etc., para un período de tiempo fijado. El tiempo para el scrapeo se fijó en dos días anteriores a la fecha de scrapeo, pero esto puede ser fácilmente adecuado al gusto del usuario, modificando la variable "days_ago" del documento [main_scraping](https://github.com/dapivei/webscraping/blob/master/main_scraping.py). **Nota:** El código podría fácilmente adecuarse para el scrapeo de otras páginas.

El *script* principal, que orquesta todas las operaciones necesarias para realizar el scrapeo, es el documento [main_scraping](https://github.com/dapivei/webscraping/blob/master/main_scraping.py), mismo que se apoya en otros dos scripts que contienen funciones auxiliares: [auxiliar_functions](https://github.com/dapivei/webscraping/blob/master/auxilar_functions.py) y [functions_pagina_siete](https://github.com/dapivei/webscraping/blob/master/functions_pagina_siete.py).

Para correr el código, situares sobre la línea de comandos y ejecutar el siguiente código:

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


**Documentos adicionales:** Además de los documentos mencionados, en el documento [selenium_newspaper_scraper](https://github.com/dapivei/webscraping/blob/master/selenium_newspaper_scraper.ipynb), puede encontrar el notebook asociado a los tres documentos antes mencionados, juntos con los outputs esperados. También, puede remitirse al documento [beautifulsoup_newspaper_scraper](https://github.com/dapivei/webscraping/blob/master/beautifulsoup_newspaper_scraper.ipynb), documento en el cuál se implementó un scrapeo de la página principal de https://www.eldiario.net, empleando la paquetería `beautifulsoup4`.

**2.** Código que permite recoger todos los tweets (mediante un scraper) de los últimos 7 días de la cuenta de Nelson Peredo (@nperedo).la API de twitter, Tweepy, (https://www.tweepy.org,), https://github.com/bisguzar/twitter-scraper.
