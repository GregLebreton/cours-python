#!/usr/bin/python


reponse=raw_input("es-tu heureux? (oui ou non): ")
if reponse == "oui":
	print "contamine tes voisins, la flamme de la joie ne se tari pas en se transmettant!"
elif reponse == "non":
	reponse2=raw_input("cela vous convient-il? (oui ou non): ")=="oui":
		print "dommage"
	elif reponse2 == "non":
		print "cherche une autre personne heureuse"
else:
		print "je n'ai pas compris la reponse"


# autre maniere:
'''

heureux=raw_input("es-tu heureux? (oui ou non): ")
if heureux == "oui":
	print "contamine tes voisins, la flamme de la joie ne se tari pas en se transmettant!"
elif raw_input("cela vous convient-il? (oui ou non): ")=="oui":
	print "dommage"
else:
	print "cherche une personne heureuse"

'''
