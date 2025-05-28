import os, urllib3

import bs4

HTTP = urllib3.PoolManager()


def cria_diretorios(caminho, diretorios = []):

    for diretorio in diretorios:

        cria_diretorio(caminho, diretorio)

    return True


def cria_diretorio(caminho, diretorio):

    if diretorio in os.listdir(caminho): pass

    else: os.makedirs(os.path.join(caminho, diretorio))

    return os.path.isdir(os.path.join(caminho, diretorio))


def extrai_texto(sopa):

    paragrafos = sopa.find_all('p')

    texto = ''
    
    for p in paragrafos:

        texto +=  p.get_text()

    return texto


def batiza_arquivo(diretorio, url, numero_da_visita):

    try:

        n = url.split('/')[-1]
    
    except: 

        n = 'deu_merda_'+str(numero_da_visita)

    nome = n + '.txt'

    return os.path.join(diretorio, nome)


def cria_arquivo(floc, texto):
    
    arq = open(floc, 'w')
    arq.write(texto)
    arq.close()
    
    return True


def visita_paginas(urls, dir_de_armazenamento):
    
    visitas = 0
    
    for i in range(2):
        
        mais_urls = set()
    
        for url in urls:

            markup = visita_e_raspa(url)
            sopa = faz_sopa(markup)
            links = extrai_links(sopa)

            floc = batiza_arquivo(dir_de_armazenamento, url, visitas)
            texto = extrai_texto(sopa)
            cria_arquivo(floc, texto)

            visitas += 1
            
            for el in links:

                link = filtra_link(el)

                if link: mais_urls.add(link)

            print(visitas, ' => visitei a url ', url, ' e coletei os links ', links)
        
        urls = mais_urls
        #print('a lista de visita agora é ', urls)

    print('acabou...')


def faz_sopa(html): return bs4.BeautifulSoup(html, 'html.parser')

def visita_e_raspa(url):
    
    r = HTTP.request('GET', url)

    if r.status in [200, '200', '200 OK']: 

        return str(r.data)

    else: 
        
        print('a pagina ', url, ' retornou ', r.status)
        return ''



def extrai_links(sopa): 
    
    ls = []
    
    links = sopa.select("a[href*='article']")
    
    for link in links: ls.append(link.attrs['href'])
    
    return ls


def filtra_link(link):

    prefixo = 'https://www.bbc.com'

    if link.startswith('/'): link = prefixo+ link

    return link
