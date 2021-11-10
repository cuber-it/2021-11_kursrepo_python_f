#list comprehension:
l = [n for n in [1,2,3,4,5,6,7,8,9] if n > 4]
print(l)

# dictionary comprehension:

d = {}
for x in ['lala','lala','lolo']:
    for y in range(10):
        if not x in d:
            d[x] = y

d = {k:v for k in ['a','b','c','d','e'] for v in [0,2,3,5,7]}
print(d)

def checker(number):
    if number %2 == 0:
        return True
    return False

iterator = filter(checker,[1,2,3,4,5,6,7,8,9,10])
print(list(iterator))