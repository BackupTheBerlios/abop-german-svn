#!/usr/bin/python

# Das ist meine Einkaufsliste.
einkaufsliste = ['Aepfel', 'Mangos', 'Karotten', 'Bananen']

print 'Ich habe ', len(einkaufsliste), 'Dinge einzukaufen.'

print 'Diese Dinge sind:', # Achten Sie auf das Komma am Ende.
for ding in einkaufsliste:
	print ding,

print '\nIch muss auch Reis einkaufen.'
einkaufsliste.append('Reis')
print 'Meine Einkaufsliste ist jetzt', einkaufsliste

print 'Jetzt werde ich meine Einkaufsliste sortieren.'
einkaufsliste.sort()
print 'Die sortierte Einkaufsliste ist', einkaufsliste

print 'Das erste Ding, das ich kaufen werde, ist', einkaufsliste[0]
altesding = einkaufsliste[0]
del einkaufsliste[0]
print 'Ich habe', altesding, 'gekauft'
print 'Meine Einkaufsliste ist jetzt', einkaufsliste

