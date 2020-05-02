"""
    Código para Scrapear la página web de Página Siete los últimos dos días. 

    Autora del Código: Camila Blanes
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())  # automatically detects the path where
                                                            # \chromedriver was installed

def obtain_title(webdriver):
    """
    Parameters
    ----------
    webdriver: drive Selenium object
        
    
    Returns
    -------
    title: str
        Title of Article
    """
    try:
        title = webdriver.find_elements_by_class_name("titular")[0].text
        return(title)
    except:
        no_title = 'minor error'
        print('Check for title')
        return(no_title)

def get_section(webdriver):
    """
    Parameters
    ----------
    webdriver: driver selenium object
    
    Returns
    -------
    section: str
        Section of Article (Ex, opinion, economy, politics, etc)
    """
    try:
        section = webdriver.find_elements_by_class_name("seccion")[0].text
        return(section)
    except:
        no_section = 'minor error'
        print('Check for content section')
        return(no_section)
    
def obtain_detail(webdriver):
    """
    Parameters
    ----------
    webdriver: drive Selenium object
        
    
    Returns
    -------
    title: str
        Detail of Article
    """
    try:
        detail = webdriver.find_elements_by_class_name("bajada")[0].text
        return(detail)
    except:
        no_detail = 'minor error'
        print('Check for detail')
        return(no_detail)

def get_body(webdriver):
    """
    Parameters
    ----------
    webdriver: driver selenium object
    
    Returns
    -------
    full body: str
        Body of Article
    """
    try:
        full_body = []
        for i in range(len(webdriver.find_elements_by_class_name('cuerpo-nota')[0].find_elements_by_tag_name("p"))):
            full_body.append(webdriver.find_elements_by_class_name('cuerpo-nota')[0].find_elements_by_tag_name("p")[i].text)
        full_body = '.'.join(full_body)
        return(full_body)
    except:
        no_body ='mayor error'
        print('Check for body')
        return(no_body)

def get_author(webdriver):
    """
    Parameters
    ----------
    webdriver: driver selenium object
    
    Returns
    -------
    author: str
        Author of the article
    """
    try:
        author = webdriver.find_elements_by_class_name('cuerpo-nota')[0].find_elements_by_tag_name("p")[0].text
        author = author.split('/')[0]
        author = re.sub(' +', '', author)
        return(author)
    except:
        no_author = 'mayor error'
        print('Check for author')
        return(no_author)

def get_errors(output_dict):
    key_ = next(iter(output_dict))
    errors_list = []
    for i in range(len(output_dict[key_])):

    	keys = ['id', 'title', 'detail', 'date', 'section', 'body_article', 'newspaper']
    	temp_list = []
    	for j in keys:
    		if output_dict[key_][i][j] == 'minor error':
    			temp_list.append(['minor error', j, output_dict[key_][i]['url_article']])
    		elif output_dict[key_][i][j] == 'mayor error':
    			temp_list.append(['mayor error', j, output_dict[key_][i]['url_article']])
    		else:
    			continue

    	if any(temp_list):
    		errors_list.append(temp_list)
    	else:
    		continue
    
    errors_list = functools.reduce(operator.iconcat, errors_list, [])
    data_frame = pd.DataFrame(errors_list, columns = ['type_error', 'key_', 'url_article'])
    return(data_frame)

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)


def get_date(article):
	try:
		date_raw = re.findall('([0-9]{4}/[0-9]+/[0-9+])', article)[0]
		year, month, day = date_raw.split('/')
		date = datetime.datetime(int(year), int(month), int(day))
		return(date)
	except:
		print('no date found')

def counter_authors(dict_output):
    authors = []
    key_ = next(iter(dict_output))
    for i in range(len(dict_output[key_])):
        authors.append(dict_output[key_][i]['author'])
    
    counts_authors = dict((x,authors.count(x)) for x in set(authors))
    data_frame = pd.DataFrame(counts_authors.items(), columns=['author', 'number_articles'])
    return(data_frame)
