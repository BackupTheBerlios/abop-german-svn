#!/usr/bin/python
# Dateiname: break.py

while True:
	s = raw_input('Geben Sie etwas ein : ')
	if s == 'ende':
		break
	print 'Die Laenge des Strings ist', len(s)
print 'Fertig'
