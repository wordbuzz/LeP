import os
import urllib3
#import pathlib

#HOME = pathlib.Path(__file__).parent.resolve()

portal = "https://www.bbc.com/"
pagina =  '/future/article/20250425-the-fibonacci-sequence-hidden-in-liverpool-fcs-premier-league-football-title'

diretorio_html = 'html'
arquivo = 'liverpool.html'
floc = os.path.join(diretorio_html, arquivo)
#floc = os.path.join(HOME, diretorio_html, arquivo)

conn = urllib3.connection_from_url(portal)
r = conn.request('GET', pagina)

arq = open(floc, 'w')
conteudo = arq.write(str(r.data))
arq.close()
