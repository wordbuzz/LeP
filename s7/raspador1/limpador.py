import os
import bs4
#import pathlib


#HOME = pathlib.Path(__file__).parent.resolve()


diretorio_html = 'html'
arquivo_html = 'liverpool.html'

floc_html = os.path.join(diretorio_html, arquivo_html )

arq = open(floc_html, 'r')
html = arq.read()


sopa = bs4.BeautifulSoup(html, 'html.parser')
arq.close()

parags = sopa.find_all('p')

#links = sopa.select("a[href*='article']")
#for link in links:
    #print(link.attrs['href'])
    #print()


diretorio_txt = 'textos'
arquivo_txt = 'liverpool.txt'

floc_txt = os.path.join(diretorio_txt, arquivo_txt)

arq = open(floc_txt, 'w')
	
texto = []
for p in parags: 

    t = p.get_text ()
    texto.append(t)
    arq.write(t)

arq.close()
