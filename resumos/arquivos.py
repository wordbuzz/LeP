s = 'vou criar uma string com algumas palavras e sem muita pontuação'

arq1 = open('meu_arquivo1.txt', 'w')
arq1.write(s)
arq1.close()


arq2 = open('meu_arquivo2.txt', 'w')
ls = s.split()
for el in ls:
    arq2.write(el)
arq2.close()

arq3 = open('meu_arquivo3.txt', 'w')
ls = s.split()
for el in ls:
    arq3.write(el+'\n')
arq2.close()


arq1 = open('meu_arquivo1.txt', 'r')
print(arq1.read())

arq2 = open('meu_arquivo2.txt', 'r')
conteudo = arq2.read()
print(conteudo)


arq3 = open('meu_arquivo3.txt', 'r')
conteudo_ = arq3.read()
print(conteudo_)

