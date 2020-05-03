
# =================== Funciones auxiliares para scrapear =======================
# Funciones auxiliares al documento principal "main_scraping.py", que sirven para
# \obtener datos relevantes que permiten el scrapeo de las noticias del periódico
# \https://www.eldiario.net
# ==============================================================================

# ===================== Importando paquetería empleanda ========================


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
from uuid import uuid4
import re
import itertools
import functools
import operator
from datetime import date, timedelta
import pandas as pd
import json
from tqdm import tqdm
import sys
sys.path.append('./webscraping')
import functions_pagina_siete as func
import auxilar_functions as auxfunc


def get_dates(days_ago):
    """
    Función que permite obtener una lista de fechas para las cuáles se hará el
    scrapeo de la página.

    Parameters
    ----------
    days_ago: fijar el tiempo para el scrapeo en días anteriores a la fecha actual


    Returns
    -------
    dates: lista de fechas
    """
    import datetime
    from datetime import date, timedelta
    import pandas as pd

    start_dt = (date.today()-timedelta(days_ago))
    end_dt = date.today()
    dates = []
    for dt in pd.date_range(start_dt, end_dt):
        dates.append(dt.strftime("%Y-%m-%d"))
    return(dates)


def get_urls(dates):
    """
    Función que permite obtener una lista de urls para las cuáles se hará el
    scrapeo de la página.

    Parameters
    ----------
    dates: lista de fechas


    Returns
    -------
    all_urls: lista de urls sobre los cuáles se hará el scrapeo de noticias
    """
    import re
    all_urls = []
    for date in dates:
        year = re.split('-', date)[0]
        month = re.split('-', date)[1]
        day = re.split('-', date)[2]
        url = 'https://www.paginasiete.bo/archivo/' + year + '/' + month + '/' + day
        all_urls.append(url)

    return all_urls

def get_links(all_urls):

    """
    Parameters
    ----------
    all_urls: lista de urls


    Returns
    -------
    flatten_list: lista sobre la cuál se hará el scrapeo
    """
    import functions_pagina_siete as func
    import functools

    all_links_week = []
    for url in all_urls:
        func.driver.get(url)

        links_page = []
        for s in range(len(func.driver.find_elements_by_class_name("archivo"))):
            func.driver_section = func.driver.find_elements_by_class_name("archivo")[s]

            len_links = len(func.driver_section.find_elements_by_class_name("listado-noticias")[0].find_elements_by_tag_name("li"))
            temp_link = []
            for l in range(len_links):
                link = func.driver_section.find_elements_by_class_name("listado-noticias")[0].find_elements_by_tag_name("li")[l].find_element_by_css_selector('a').get_attribute('href')
                temp_link.append(link)
            links_page.append(temp_link)
        all_links_week.append(links_page)

    list_pages = functools.reduce(operator.iconcat, all_links_week, [])
    flatten_list = functools.reduce(operator.iconcat, list_pages, [])
    return(flatten_list)

def webscraping(flatten_list):

    """

    Función que obtiene el título, autor, detalles, fechas, secciones y cuerpo
    de los artículos sobre los cuales se realizó el scrapeo.

    Parameters
    ----------
    flatten list: lista sobre la cuál se hará el scrapeo


    Returns
    -------
    df: dataframe con las siguientes columnas- id, title, author, detail, date,
    section, body_article
    """
    import functions_pagina_siete as func
    articles_pagina_siete = {'week_x' : {}}
    list_articles = []
    for i in range(len(flatten_list)):
        func.driver.get(flatten_list[i])

        temp = {}
        temp['id'] = str(uuid4())
        temp['title'] = func.obtain_title(func.driver)
        temp['author'] = func.get_author(func.driver)
        temp['newspaper'] = 'pagina_siete'
        temp['detail'] = func.obtain_detail(func.driver)
        temp['date'] = func.get_date(flatten_list[i])
        temp['section'] = func.get_section(func.driver)
        temp['body_article'] = func.get_body(func.driver)

        list_articles.append(temp)
        #print('Finish ', i, '/', len(flatten_list))
    articles_pagina_siete['week_x'] = list_articles

    func.driver.close()  #closing driver
    df = pd.DataFrame(data=list_articles, columns=['id', 'title', 'author', 'newspaper', 'detail', 'date', 'section', 'body_article'])
    return(df)
