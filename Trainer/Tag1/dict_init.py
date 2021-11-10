# Dict Comprehension
d = { n: n**2 for n in range(1,11) }
print(d)

# List comprehension mit dict-cast
d = dict([(n, n**2) for n in range(1,11)])
print(d)

# Zwei-Listen zip mit dict-cast
z = dict(zip([1,2,3,4,5],[1,4,9,16,25]))
print(z)

