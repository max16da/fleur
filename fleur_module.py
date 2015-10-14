#! /usr/bin/python
# -*- coding: utf-8-unix; -*- 

# En-tête du module et déclaration des objets et fonctions de celui-ci
#

#~ if __name__ == "__main__":
	#~ # Code du corps principal

phrase="";	
	
#fonction qui interroge l'utilisateur
def donnees_utilisateur():
	sexe=raw_input("Es-tu un garçon ou une fille (g/f) ? ");
	if (sexe == "g"):
		sujet = "Elle"
	elif (sexe == "f"):
		sujet = "Il"
	else:
		print "Tape 'g' si tu es un garçon ou 'f' si tu es une fille. Relance le programme."
		exit()
	nb_petales=int(raw_input("Entre le nombre de pétales de la fleur: "))
	
	
def recupere_donnees():
	mots_ritournelle = ["m'aime", "un peu", "beaucoup", "passionnément", "à la folie", "pas du tout"]
	n = 1
	num_mot = 0
	while n <= nb_petales:
		if num_mot == 0:
			phrase = phrase + sujet + " "
		if num_mot > 0:
			phrase = phrase + ", "
		phrase = phrase + mots_ritournelle[num_mot]
		n = n + 1
		if num_mot < len(mots_ritournelle) - 1:
			num_mot = num_mot + 1
		else:
			phrase = phrase + ".  "
			num_mot = 0
	
def affiche():
	recupere_donnees();
	print phrase;

affiche();
