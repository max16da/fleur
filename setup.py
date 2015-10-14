
import pydoc


pydoc.importfile('/path/to/script_fleur.py')
pydoc script_fleur > doc_script_fleur.txt


import sys

filename = sys.argv[1]
text = open(filename, 'rb').read().replace('\r\n', '\n')
open(filename, 'wb').write(text)
