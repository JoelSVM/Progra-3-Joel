import random
import collections

n=6
aleatorios = [random.randint(0,10) for _ in range(n)]
print "estos son los randoms ",aleatorios

repetido = []
unico = []
for x in aleatorios:
	if x not in unico:
		unico.append(x)
	else:
		if x not in repetido:
			repetido.append(x)
 
print "estos son los unicos ", unico

if(repetido==[]):
    print" no se encontro nigun repetido -1"
else:
    print "estos son los repetidos ", repetido
    





