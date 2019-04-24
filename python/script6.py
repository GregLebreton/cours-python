#!/usr/bin/python

l=[1,1]
tailledesiree=input("saisir la taille de la liste voulue: ")
nb=len(l)

def fonctionliste(l):
    nouveau=l[-1]+l[-2] # nouveau = dernier nombre de la liste + avant dernier
    l.append(nouveau) #on ajoute nouveau a la fin de la liste
    return l

for x in range (1,tailledesiree):
    liste=fonctionliste(l)
    print (liste)



