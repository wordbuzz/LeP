from tarefas import *

urls = ['https://www.bbc.com/culture/article/20250501-the-terrifying-stunts-of-a-french-film-legend',
	'https://www.bbc.com/travel/article/20250505-where-to-get-new-york-citys-best-chinese-food']

SUBDIR = 'textos'

markups = visita_paginas(urls)
textos = extrai_textos(markups)
cria_arquivos(SUBDIR, textos)
