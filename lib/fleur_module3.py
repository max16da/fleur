#! /usr/bin/python
# -*- coding: utf-8-unix; -*- 

suject=[]
phraseFinale=[];


# Donner un message d'introduction pour décrire ce que fait le programme
print """Ce programme s'adresse à vous, utilisateur.

Il va effeuiller pour vous les pétales d'une fleur et vous compter la
ritournelle d'amour bien connue.

Pour cela, il a besoin de savoir si vous êtes un garçon ou une fille et
combien de pétales il y a sur la fleur.

"""	
#fonction qui interroge l'utilisateur
# Demander à l'utilisateur les informations d'entrée pour lancer le programme:
#  - s'il est un garçon ou une fille
#  - le nombre de pétales de la fleur
def donnees_utilisateur():	
	sexe=raw_input("Es-tu un garçon ou une fille (g/f) ? ");
	if (sexe == "g"):
		sujet = "Elle"
	elif (sexe == "f"):
		sujet = "Il"
	else:
		print "Tape 'g' si tu es un garçon ou 'f' si tu es une fille. Relance le programme."
		exit()
	suject.append(sujet)
	#~ recupere_donnees(suject)

#fonction qui récupère et affiche le résultat à l'utilisateur	
def recupere_donnees():
	nb_petales=int(raw_input("Entre le nombre de pétales de la fleur: "))
	mots_ritournelle = ["un peu", "beaucoup", "passionnément", "à la folie", "pas du tout"]	

#contruction de la phrase selon l'effeuillement
	ritournelle = []
	for mot in mots_ritournelle:
		ritournelle.append(mot + ", ")
	ritournelle[-1]=ritournelle[-1].replace(", ", ".  ")
	ritournelle.insert(0, str(suject) + " m'aime, ")	
	
# Construction de la phrase à partir de la liste des chaînes élaborée
	n = 0
	phrase=""
	while n < nb_petales:
		# L'indice du mot est borné à la longueur de la liste par l'opérateur "%"
		num_mot = n % len(ritournelle)
		phrase = phrase + ritournelle[num_mot]
		n = n + 1

	phrase = phrase.rstrip(", ")
	print phrase


# En-tête du module et déclaration des objets et fonctions de celui-ci
if __name__ == "__main__":
	donnees_utilisateur()
	recupere_donnees()
