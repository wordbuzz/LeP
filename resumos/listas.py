trapas = ['Didi', 'Dedé', 'Mussum', 'Zacarias']
beatles = ['John', 'Paul', 'George', 'Ringo']
apocalipse = ['fome','guerra','praga','morte']

quartetos = [trapas, beatles, apocalipse, 4, '4']
primos = [11, 13, 17, 19, 23]
#slicing é semelhante as strings
#trapas[0] #'Didi'
#trapas[-1] #'Mussum'
#etc

apocalipse.append('inganeis')

primos.append(27)
primos.pop()
primos.index(17)#2 posição do int 17

for numero in primos:
    if numero >= 11 and numero<20:
        print(numero)
    else: print('!')
