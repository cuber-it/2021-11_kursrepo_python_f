a=[x+1 for x in range(5) if x>2]
print(a)
# funktioniert

l=[x**2 for x in [1, 2, 3, 4]]
print(l)
# funktioniert

#-----------------------------------------
# ASCII Tabelle als dictionary
 
b={table: chr(table) for table in range(32, 128)}
# chr steht für character
print(b)
# funktioniert