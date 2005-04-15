#!/usr/bin/python

import sys

print 'Die Kommandozeilen-Argumente sind:'
for i in sys.argv:
	print i

print '\n\nDer PYTHONPATH ist', sys.path, '\n'
