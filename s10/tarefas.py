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


def cria_arquivos(caminho, conteudos, extensao = '.txt'):

    for i, conteudo in enumerate(conteudos):

        nome = str(i) + extensao

        floc = os.path.join(caminho, nome)

        cria_arquivo(floc, conteudo)


def cria_arquivo(floc, conteudo): pass

def visita_paginas(urls):
    
    visitas = 0
    
    for i in range(3):
        
        mais_urls = set()
    
        for url in urls:

            markup = visita_e_raspa(url)
            sopa = faz_sopa(markup)
            links = extrai_links(sopa)

            visitas += 1
            
            for el in links:

                link = filtra_link(el)

                if link: mais_urls.add(link)

            print(visitas, ' => visitei a url ', url, ' e coletei os links ', links)
        
        urls = mais_urls
        #print('a lista de visita agora é ', urls)

    print('acabou...')


def faz_sopa(html): return bs4.BeautifulSoup(html, 'html.parser')

def extrai_textos(sopa): pass


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
