import pathlib

from tarefas import *

HOME = pathlib.Path(__file__).parent.resolve()

SEMENTE = ['https://www.bbc.com/news/articles/cqj77pgyq81o']

cria_diretorios(HOME, diretorios = 'html textos'.split())
markups = visita_paginas(SEMENTE)
#textos = extrai_textos(markups)
#salva_arquivos('textos', textos)
