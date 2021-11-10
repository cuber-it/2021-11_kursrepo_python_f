#import basis
import basis_copy as basis

o1 = basis.Basis()
o2 = basis.Basis("Erster Wert")

o1.read()

o1.write()
o2.write()

o1.bearbeite_text()
o2.bearbeite_text()

o1.write()
o2.write()

basis.Basis("Ein Text").bearbeite_text().write() # das geht wegen der return self in den MEthoden
o3 = basis.Basis().read().bearbeite_text().write()
o3.write()


basis.Basis().read(open("/home/coder/Workspace/aktueller-kurs/Materialien/config.yaml")).bearbeite_text().write()

