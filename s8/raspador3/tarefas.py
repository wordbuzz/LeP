import os, urllib3

import bs4

HTTP = urllib3.PoolManager()

PROTOCOLO = 'https://'
PORTAL = 'www.bbc.com'

paginas = ['/culture/article/20250501-the-terrifying-stunts-of-a-french-film-legend',
	'/travel/article/20250505-where-to-get-new-york-citys-best-chinese-food']


visitadas = []

TEXTOS_DIR = 'textos'
HTML_DIR = 'html'

if not os.path.isdir(HTML_DIR): os.mkdir(HTML_DIR)

if not PORTAL in os.listdir(HTML_DIR): 

    os.mkdir(os.path.join(HTML_DIR, PORTAL))


if not os.path.isdir(TEXTOS_DIR): os.mkdir(TEXTOS_DIR)

if not PORTAL in os.listdir(TEXTOS_DIR): 

    os.mkdir(os.path.join(TEXTOS_DIR, PORTAL))

##################
for pagina in paginas:

    pagina_split = pagina.split('/')
    nome = pagina_split[-1]

    url = PROTOCOLO + PORTAL + pagina

    r = HTTP.request('GET', url)

    
    if r.status in [200, '200', '200 OK']: 

        pass #print('visitando', url, r.status)

    else: 
        
        print('deu m*! a pagina ', url, ' retornou ', r.status)
        continue

    html = str(r.data)
    sopa =  bs4.BeautifulSoup(html, 'html.parser')

    paragrafos = sopa.find_all('p')

    texto = ''
    
    for p in paragrafos:

        texto +=  p.get_text()



    floc = os.path.join(HTML_DIR, PORTAL, nome + '.html')
    arq = open(floc, 'w')
    arq.write(html)
    arq.close()
   

    floc = os.path.join(TEXTOS_DIR, PORTAL, nome + '.txt')
    arq = open(floc, 'w')
    arq.write(texto)
    arq.close()


    links = sopa.find_all('a')

    for link in links:


        href = link.attrs['href']
        print(href)


        if 'article' not in href:  continue 
        elif not 'bbc' in href: continue
        elif href.startswith('www'): continue
        elif href.startswith('http'): continue

        else:

            if len(visitadas) < 50: 

                paginas.append(href)


    paginas.remove(pagina)







def cria_arquivo(path, arqid, conteudo):
    
    floc = os.path.join(path, arqid)
    arq = open(floc, 'w')
    arq.write(conteudo)
    arq.close()
    return True

def le_arquivo(path, arqid): pass


###################
def visita_paginas(urls):

    ls = []
    
    for url in urls: 

        ls.append(visita_pagina(url))

    return ls


def visita_pagina(url):

    r = HTTP.request('GET', url)

    if r.status in [200, '200', '200 OK']: 

        return str(r.data)

    else: 
        
        print('a pagina ', url, ' retornou ', r.status)
        return ''

def processa_paginas(urls):

    a_visitar = copy.deepcopy(urls)

    for url in a_visitar:

        html = visita_pagina(url)


########################

def processa_sopa(html):
    
    sopa = faz_sopa(html)
    texto = extrai_texto(sopa)
    links = extrai_links(sopa)

    return texto, link

def faz_sopa(html):
    
    return bs4.BeautifulSoup(html, 'html.parser')


def extrai_textos(markups):

    textos = []
    for markup in markups:

        textos.append(extrai_texto(markup))
    
    return textos


def extrai_texto(sopa):

    paragrafos = sopa.find_all('p')

    texto = ''
    
    for p in paragrafos:

        texto +=  p.get_text()

    return texto

def extrai_links(sopa):
    
    return sopa.find_all('a')


def filtra_links(links, filtro):
    
    filtrados = []
    
    for l in links:

        href = l.attrs['href']

        if filtro in href: filtrados.append(href)

    return filtrados

