#!/usr/bin/python


#liste=[1,2,3]
#liste=[1,2]
liste=[1,2,3,4,5]

count=len(liste)

if count > 3:
	del liste[count-1]
	print liste
elif count < 3:
	liste.append(3)
	print liste
else count == 3:
	del liste[count-1]
	print liste
