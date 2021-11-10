import this

l1=["a","b","c"]
l2=[1,2,3]
z=zip(l1,l2)
l=list(z)
d=dict(zip(l1,l2))    # zip ist auch ein generator und wird verbraucht
print(l)
print(d)

