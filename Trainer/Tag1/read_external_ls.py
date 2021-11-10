from subprocess import Popen, PIPE

def read_ls(folder):
    result = None
    # legt einen externen Prozess an, in dem ein anderes Kommando ausgeführt wird
    process = Popen(["ls", "-la", folder], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    if exit_code == 0:
        result = str(output).split(r"\n")
    return result

if __name__ == "__main__":
    l = read_ls("/bin")
    groesse = 0
    for n in l[1:-1]:
        groesse += int(n[24:31])
    print("Gesamt:", groesse, " Byte")

    groessen_liste = []
    for n in l[1:-1]:
        v = int(n[24:31])
        if v < 1000:
            groessen_liste.append(int(n[24:31]))
    print("Einzelgrössen:", groessen_liste)

    # als List-Comprehension kürzer dargestellt
    groessen_liste = [int(n[24:31]) for n in l[1:-1] if int(n[24:31]) < 1000]
    print("Einzelgrössen:", groessen_liste)
