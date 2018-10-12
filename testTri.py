#!/usr/bin/env python3
# coding: utf-8

from time import clock
import numpy

def triBulle(l):

	triee = False
	L = len(l)
	etape = L-1

	while (not triee):

		i = 0
		triee = True

		while (i < etape):

			if (l[i] > l[i+1]):

				triee = False
				aux = l[i]
				l[i] = l[i+1]
				l[i+1] = aux

			i += 1
		etape -= 1

#insérer l'élément e à l'indice i dans la liste l
def inserer(l,i,e):
	return l[:i] + [e] + l[i:]


def triInsertion(l):

	listeTriee = []
	L = len(l)
	i = 0

	while (i < L):

		j = 0
		LT = len(listeTriee)
		ajout = False
		element = l[i]

		while (j < LT):

			if (element < listeTriee[j]):

				listeTriee = inserer(listeTriee,j,element)
				ajout = True
				break

			j += 1

		if (not ajout):

			listeTriee.append(element)

		i += 1

	return listeTriee

#fusionne deux listes triees
def fusion(l1,l2):

	listeFusionnee = []
	i1 = 0
	i2 = 0
	L1 = len(l1)
	L2 = len(l2)

	while (i1 < L1 and i2 < L2):

		if(l1[i1] < l2[i2]):

			listeFusionnee.append(l1[i1])
			i1 += 1

		else:

			listeFusionnee.append(l2[i2])
			i2 += 1

	if (i1 < L1):

		listeFusionnee = listeFusionnee + l1[i1:]

	else:

		listeFusionnee = listeFusionnee + l2[i2:]

	return listeFusionnee

def triFusion(l):

	L = len(l)

	if(L < 2):

		return l

	else :

		return fusion(triFusion(l[:int(L/2)]),triFusion(l[int(L/2):]))





l = [5,3,8,4,5,9,2,5,4,6,5,3,8,1,7,8,4,3,9]

lAlea = numpy.random.randint(1,100,1000)


print("liste non triée : " + str(l))

tempsDebut = clock()*1000
triBulle(l)
tempsFin = clock()*1000

print("liste triée : " + str(l))

print("durée d'exécution de triBulle (en ms): " + str(tempsFin - tempsDebut))

l = [5,3,8,4,5,9,2,5,4,6,5,3,8,1,7,8,4,3,9]

print("liste non triée : " + str(l))

tempsDebut = clock()*1000
l = triInsertion(l)
tempsFin = clock()*1000

print("liste triée : " + str(l))

print("durée d'exécution de triInsertion (en ms) : " + str(tempsFin - tempsDebut))

l = [5,3,8,4,5,9,2,5,4,6,5,3,8,1,7,8,4,3,9]

print("liste non triée : " + str(l))

tempsDebut = clock()*1000
l = triFusion(l)
tempsFin = clock()*1000

print("liste triée : " + str(l))

print("durée d'exécution de triFusion (en ms) : " + str(tempsFin - tempsDebut))

print(lAlea)
print("test sur liste aleatoire de longueur " + str(len(lAlea)))
print("triInsertion")
tempsDebut = clock()
triInsertion(lAlea)
tempsFin = clock()
print(tempsFin - tempsDebut)

print("triFusion")
tempsDebut = clock()
triFusion(lAlea)
tempsFin = clock()
print(tempsFin - tempsDebut)

print("triBulle")
tempsDebut = clock()
triBulle(lAlea)
tempsFin = clock()
print(tempsFin - tempsDebut)

print(lAlea)
