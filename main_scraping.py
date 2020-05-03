#!/usr/bin/python
# -*- coding: utf-8 -*-


# =========== Código para principal para scrapear con selenium  ================
#
# Objetivo: con este código se scrapea noticias de https://www.eldiario.net
#
# Notas: con la variable "days_ago", establecemos cuántos días, anteriores a la
# \fecha de la fecha actual, queremos scrapear las noticias. Por default, se
# \estableció el tiempo para el scrapeo en dos días anteriores a la fecha actual
#
# Funciones auxiliares: el script se apoya en dos documentos .py que contienen
# \funciones.
#
# Output: el output de este script es un documento .csv
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
import functions_pagina_siete as func          # .py con funciones auxiliares
import auxilar_functions as auxfunc            # .py con funciones auxiliares


days_ago = 2                                   # determines from how many days
                                               # \ago we wish to scrap
                                               # \news from the newspaper

dates = auxfunc.get_dates(days_ago)
                                               # gets dates we will scrap

all_urls = auxfunc.get_urls(dates)              # gets all_urls of the specified
                                               # \dates


flatten_list = auxfunc.get_links(all_urls)      # getting links of specified
                                               # \urls

df = auxfunc.webscraping(flatten_list)         # webscraping information from
                                               # \specified links and returns data
                                               # \in a dataframe

df.to_csv('paginasiete.csv')                   # saving dataframe in .csv
