d = {'machado': 'rio',
     'ubaldo': 'salvador',
     'joyce': 'dublin'}

d['graciliano'] = 'quebrangulo'
d['drummond'] = 'itabira'
d.items()

for k, v in d.items():
    print(k,v)

print('machado' in d)#True
print('rio' in d)#False
