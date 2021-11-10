a = range(1,10)
print(a)
print(type(a))
for n in a: # for n in [0,1,2,3,4,5,6,7,8,9, ...]
    print(n)


def my_range(start, stop):
    lfd_wert = start
    while lfd_wert < stop:
        yield lfd_wert
        lfd_wert += 1

b = my_range(1, 10)
print(b)
print(type(b))
for n in b:
    print(n)