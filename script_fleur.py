#! /usr/bin/python
# -*- coding: utf-8-unix; -*- 
#
############################################################################### 
#
# Outil: script_fleur.py
#    Atelier "Art de la programmation" - illustre la rédaction d'un script.
#    Fonctionnalité: Affiche une ritournelle pour l'effeuillage d'une fleur.
#
#============================================================================== 
#
# Auteur et Licence: 
#  (C) 2014 AGPLv3, C. Schockaert <R3vLibre@citadels.be>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation; version 3.
#
###############################################################################

# Donner un message d'introduction pour décrire ce que fait le programme
print """Ce programme s'adresse à vous, utilisateur.

Il va effeuiller pour vous les pétales d'une fleur et vous compter la
ritournelle d'amour bien connue.

Pour cela, il a besoin de savoir si vous êtes un garçon ou une fille et
combien de pétales il y a sur la fleur.

"""

# Demander à l'utilisateur les informations d'entrée pour lancer le programme:
#  - s'il est un garçon ou une fille
#  - le nombre de pétales de la fleur
sexe = raw_input("Es-tu un garçon ou une fille (g/f) ? ")
if (sexe == "g"):
    sujet = "Elle"
elif (sexe == "f"):
    sujet = "Il"
else:
    print "Tape 'g' si tu es un garçon ou 'f' si tu es une fille. Relance le programme."
    exit()

# Si le nombre de pétales n'est pas valide, Python se charge de remonter l'erreur
nb_petales = int(raw_input("Entre le nombre de pétales de la fleur: "))

# Effeuille les pétales de la fleur en énumérant les mots de la ritournelle
mots_ritournelle = ["m'aime", "un peu", "beaucoup", "passionnément", 
                    "à la folie", "pas du tout"]

# Construire la phrase au fur-et-à-mesure des pétales effeuillés
phrase = ""
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
        
# Affichage du résultat à l'écran
print phrase
