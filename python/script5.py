#!/usr/bin/python

'''
listedemployes=["greg","hamza","luc","henry"]

for x in listedemployes:
	print x

# autre notation
for x in range (0,5):
	print x
'''

tailleliste=input("saisir la taille de la liste")
liste=[]

for x in range (1,tailleliste+1):
	liste.append((x,x**2))
print liste