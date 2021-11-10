# Funktioniert nicht, macht range einfach nicht!
# a = range('a', 'z')
# for n in a:
#    print(n)
#

# Ein eigener Generator hilft!
def char_range(von, bis):
    zeichen = ord(von)
    ende = ord(bis)
    while zeichen <= ende:
        yield((zeichen, chr(zeichen)))
        zeichen += 1

cr = char_range(' ', 'z')

for n, c in cr:
    print(n, c)

# Alle Werte auf einmal erzeugen und in Liste speichern
crl = list(char_range(' ', 'z'))
print(type(crl))
print(crl)
