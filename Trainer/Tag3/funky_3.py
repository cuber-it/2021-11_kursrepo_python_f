def mach_was(daten, x):
    def add(a, b):
        return a + b

    result = []
    for v in daten:
        result.append(add(v, x))
    return result

e = mach_was([1,2,3,4,5], 10)
print(e)
# print(add(4,5)) - add ist nur innerhalb von mach_was sichtbar, da nur dort wo es definiert wurde ein Zugriff möglich ist
# von hier kommt man zu einem Konzept: Clojure
