#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import pydoc
import fnmatch
# Path to be created
#~ path = "~/Documents/algorithmique_artdelaprog/ateliers/ex_fleur/document/"
#~ 
#~ os.mkdir(path,0755);

def fichier():
	for root, dirs, files in os.walk(".", topdown=False):
		for name in files:
			print(os.path.join(root, name))
		for name in dirs:
			print(os.path.join(root, name))
#~ 
#~ #Récupère tous les fichiers .py
def recupere():
	for file in os.listdir('.'):
		if fnmatch.fnmatch(file, '*.py'):
			print file

def write():
	pydoc.importfile('script_fleur.py')	
	aide=pydoc.render_doc('script_fleur.py')s	
	pydoc.writedoc(script_fleur)

#~ pydoc.importfile('/path/to/script_fleur.py')

