s1 = 'eu sou uma string'
s2 = "vOCê é UmA sTRiNg TamBéM?"


#print('z' in s1) #False
#print('t' in s1) #True

#if 'z' in s1: print('###') #False
#'t' in s1: print('@@@') #True



#print(s1[0]) #e
#print(s1[1]) #u
#print(s1[3:7])#sou
#print(s1[3:])#sou uma string
#print(s1[-1])#g
#print(s1[-6:-1])#strin

#print(s1*3)

#print(s1+s2)

#print(s1.find('ou'))#4, quatro é a posição onde a string 'ou' começa
#print(s2.find('ou'))#-1, não encontrou!


ls1 = s1.split()
ls2 = s2.split('m')
#print(type(ls1), ls1)
#print(type(ls2), ls2)


#print('casa'.isalpha())#True
#print(s1.isalpha())#False
#print(s2.isalpha())#False
#print('123'.isdigit())#True


#for char in s1:
#    print(char)


#for char in s2:
#    if not char.isalpha():
#        print(char)


s1.upper()
s2.lower()
#print(s1)
#print(s2)

s1_ = s1.upper()
s2_ = s2.lower()
#print(s1_)
#print(s2_)

#print('Didi Dedé Mussum Zacarias'.split())
#print(' & 'join(['John Paul George Ringo']))
