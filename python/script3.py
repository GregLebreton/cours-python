#!/usr/bin/python

heureux=raw_input("es-tu heureux? (oui ou non): ")
daccord=raw_input("es-tu d'accord avec cette situation?")


if heureux == "oui" and daccord == "oui":
	print "irrecuperable"
elif heureux == "oui" and daccord == "non":
	print "malheureux mais content!"
elif heureux == "non" and daccord == "non":
	print "fait quelquechose bordel!"

