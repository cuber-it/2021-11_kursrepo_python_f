
a = float(input("geben Sie eine Zahl ein:"))
b = float(input("geben Sie noch eine Zahl ein:"))

try:
    z=a/b
    print("Das Ergebnis ist ", z)
except Exception as e:
    print(e)



'''
try:
    #whatever code that shall be here
    
except Errorklasse1 as e1:
    Fehlerbehandlung_whatever_x
except Errorklasse2 as e2:
    Fehlerbehandlung_whatever_y
except RuntimeError as e3:
    Fehlerbehandlung_whatever_z
finally: 
    code_der_immer_laufen_muss
'''