#!/usr/bin/python

# fonction qui donne le factoriel d'un nombre

'''

def factoriel(nb):
    if nb != 0:
        return (nb*factoriel(nb-1))
    else:
        return 1

nb=input("donner un chiffre: ")
print (factoriel(nb))

# fonction 

def mafonction(a, b=1, c=3):
    z=a+b+c
    return z

result=
result=mafonction(5)

#########################

l=[1,2,3,4,5,6]

def switch(l, a, b):
    tailleliste=len(l)
    dernier=l[0]
    premier=l[tailleliste-1]
    l.insert(0,premier)
    l.insert(tailleliste+1,dernier)
    return l

result=switch(l)
print (result)

'''
'''

# switcher premier et dernier index

liste=[1,2,3,4,5,6]

def listeSwitcher(liste, a=1, b=2):
    premier=liste[0]
    dernier=liste[-1]
    c=premier
    liste[-1]=c
    c=dernier
    liste[0]=c
    return liste

result=listeSwitcher(liste)
print (result)


# switcher avec a et b en choix user

liste=[1,2,3,4,5,6]

def listeSwitcher2(liste, a=1, b=2):
    premierIndex=input("veuillez entrer l'index de la valeur a changer: ")
    dernierIndex=input("veuillez entrer l'index de l'autre valeur a changer: ")
    x=liste[premierIndex]
    y=liste[dernierIndex]
    variableTempo=x
    liste[dernierIndex]=variableTempo
    variableTempo=y
    liste[premierIndex]=variableTempo
    return liste

result=listeSwitcher2(liste)
print (result)



liste=[1,2,3,4,5,6,7,8,9,10]

def rechercheDichotomique(liste,elementRecherche):
    milieu=((len(liste))//2)
    if liste[milieu] == elementRecherche:
        return milieu
    elif liste[milieu] > elementRecherche:
        for i in range(0, milieu):
            if elementRecherche == liste[i]:
                return i
    elif liste[milieu] < elementRecherche:
        for i in range(milieu, (len(liste))):
            if elementRecherche == liste[i]:
                return i   

result=rechercheDichotomique(liste,1)
print(result)

# FONCTION DICHOTOMIQUE RECCURSIVE

def rechercheDichotomiqueRecursive(liste,elementRecherche):
    longueur=len(liste)
    if longueur == 1:
        return 0
    else:
        liste_gauche=liste[0:longueur//2]
        liste_droite=liste[longueur//2:longueur]
        if liste_gauche[(longueur//2)-1] >= elementRecherche:
            return rechercheDichotomiqueRecursive(liste_gauche,elementRecherche)
        else:
            return (longueur//2)+rechercheDichotomiqueRecursive(liste_droite, elementRecherche)

result=rechercheDichotomiqueRecursive(liste,5)
print(result)

'''
#LES CLASSES

class Client:
    numero_client=0
    def __init__(self, name, compte):
        self.name = name
        self.compte= compte
        self.id=Client.numero_client
        Client.numero_client += 1

    def toString(self):
        print("Hello my name is " + self.name + ", mon numero de compte est le " 
        + str(self.compte.numero) + ", mon numero de client unique est le " 
        + str(self.id))


class Compte:
    def __init__(self, numero, solde):
        self.numero = numero
        self.solde = solde

    def afficherSolde(self):
        print("le solde du compte numero " + self.numero 
        + " est de : " + str(self.solde) + " euros")

    def debiterCompte(self, numCompte, montant):
        self.solde = self.solde - montant

compteCourant = Compte("456234957", 200)
client1 = Client("Greg", compteCourant)

client1.toString()
client1.compte.afficherSolde()
client1.compte.debiterCompte("456234957", 100)
client1.compte.afficherSolde()
print("le solde du compte est maintenant de " + str(client1.compte.solde))


        