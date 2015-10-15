#! /usr/bin/python
# -*- coding: utf-8-unix; -*- 
#
############################################################################### 
#
# Outil: setup.py
#    Atelier "Art de la programmation" - illustre la rédaction d'un script.
#    Fonctionnalité:Créer un dossier documentation comprenant toute la doc des fichiers .py.
#
#============================================================================== 
#
# Auteur et Licence: 
#  (C) 2014 M Girard 
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation; version 3.
#

import pydoc
import sys
import os
import fnmatch

#~ if len(sys.argv)<2:

def createDoc():
		#~ 
	path=sys.argv[1];  #nom du dossier à créer que l'on met en argument
	if not os.path.exists(path):
		os.makedirs(path)

#~ #parcours l'arborescence pour lister tous les fichiers .py
def parcours():
	for root,dirs,files in os.walk(".."):
		for filename in fnmatch.filter(files, '*.py'):
			print filename	
			#~ module_name='.'.join(filename.split('.')[:-1])	
			#~ pydoc.importfile(filename)
			#~ aide = pydoc.render_doc(module_name)
			#~ pydoc.writedoc(module_name)
	#~ pydoc.writedocs("/home/max/projets/fleur/");
			
				
if __name__ == '__main__':
	createDoc()
	parcours()


#~ filename = sys.argv[1]
#~ text = open(filename, 'rb').read().replace('\r\n', '\n')
#~ open(filename, 'wb').write(text)
