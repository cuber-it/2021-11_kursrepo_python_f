
# Filter für gerade zahlen
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even =[]
for n in numbers:
    if (n % 2 == 0):
        numbers.remove(n)
print(numbers)
# funktioniert

#---------------------------------------------
#maps = strange thing... ignorieren
#-------------------------------------------

# generator
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

f= fibonacci_gen()

counter = 0
for x in f:
    print(x)
    counter += 1
    if (counter > 10): 
        break
print
#funktioniert