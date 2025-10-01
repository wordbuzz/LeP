s = 'vou criar uma string com algumas palavras e sem muita pontuação'
ls = s.split()


o = 0
for char in s:
    if char == 'o':
        o = o + 1
print(o)

g = 0
for palavra in ls:
    for char in palavra:
        if char == 'g':
            g += 1
print(g)
