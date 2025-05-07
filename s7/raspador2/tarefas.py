import os, urllib3

import bs4

HTTP = urllib3.PoolManager()

##################
def cria_arquivos(path, conteudos):

    for i, conteudo in enumerate(conteudos):

        nome = str(i) + '.txt'
        
        try:
            
            cria_arquivo(path, nome, conteudo)

        except: 

            raise Exception('tentei criar o arquivo %s mas deu m*'%nome)

    return True


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

########################

def extrai_textos(markups):

    textos = []
    for markup in markups:

        textos.append( extrai_texto(markup))
    
    return textos

def extrai_texto(html):

    sopa = bs4.BeautifulSoup(html, 'html.parser')
    paragrafos = sopa.find_all('p')

    texto = ''
    
    for p in paragrafos:

        texto +=  p.get_text()

    return texto
