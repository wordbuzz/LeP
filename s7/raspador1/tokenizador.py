import os

diretorio_txt = 'textos'
arquivo_txt = 'liverpool.txt'

floc_txt = os.path.join(diretorio_txt, arquivo_txt)

arq = open(floc_txt, 'r')
texto = arq.read()


palavras = texto.split()

dicionario = {}


for p in palavras:

    if p in dicionario.keys(): dicionario[p] += 1

    else: dicionario[p] = 1

print(dicionario)
