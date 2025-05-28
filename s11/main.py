import pathlib

from tarefas import *

HOME = pathlib.Path(__file__).parent.resolve()

SEMENTES = ['https://www.bbc.com/culture/article/20250415-jmw-turner-at-250-why-his-greatest-painting-the-fighting-temeraire-is-so-misunderstood']
#['https://www.bbc.com/news/articles/cqj77pgyq81o']


def raspa_paginas():
	cria_diretorios(HOME, diretorios = 'html textos'.split())
	markups = visita_paginas(SEMENTES, 'textos')
	

def faz_glossario(diretorio):
	print(diretorio)

raspa_paginas()
