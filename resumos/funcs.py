import os
from pathlib import Path

home = Path(__file__).parent.resolve()
parente = Path(home).parent.resolve()

def le_arquivo(caminho):
    fh = open(caminho, 'r')
    texto = fh.read()
    fh.close()
    return texto


def cria_arquivo(caminho, conteudo):
    fh = open(caminho, 'w')
    for c in conteudo:
        fh.write(c+'\n')
    fh.close()
    return True

def tokeniza_texto(texto):
    ls = texto.split()
    
    tokens = []
    for el in ls:

        token = tokeniza_item_lexical(el)

        if not token: continue
        else: tokens.append(token)
    return tokens

def tokeniza_item_lexical(item):
    item = item.lower()
    if not item: return ''
    if not item[0].isalpha(): item = item[1:]
    
    try:
        if not item[-1].isalpha(): item = item[:-1]
    except IndexError: 
        pass
    return item


def faz_lexico(palavras):
    lexico = []
    for palavra in palavras:
        if palavra not in lexico:
            lexico.append(palavra)
    return sorted(lexico)

def armazena_lexico(parente, nome_do_arquivo):
    text_path = os.path.join(parente, nome_do_arquivo)
    texto = le_arquivo(text_path)
    tokens = tokeniza_texto(texto)
    lexico = faz_lexico(tokens)
    lex_path = os.path.join(parente, 'lexico')
    return cria_arquivo(lex_path, lexico)


def conta_palavras(): pass 




def testdrive():
    arquivo = 'joao-ubaldo-ribeiro-viva-o-povo-brasileiro.txt'
    caminho = os.path.join(parente, arquivo)
    #print(parente)
    #print(le_arquivo(caminho))
    #print(tokeniza_texto('o rato roeu a ?roupa do Rei de Roma!'))
    #print(faz_lexico('o rato roeu a roupa do rei de roma'.split()))
    #cria_arquivo('lexico', 'a rainha de raiva fez o que')
    armazena_lexico(parente, arquivo)
testdrive()
