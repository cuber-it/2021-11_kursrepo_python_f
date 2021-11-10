#!/usr/bin/bin python3
import pprint
import pandas

def read_quotes(fname, encoding="utf-8"):
    with open(fname, encoding=encoding) as file:
        return file.read().splitlines()

def prepare_quotes(raw):
    result = []  # Gesamtform ist dann [{}]
    header = raw[0].replace(" ", "").split(",")
    for zeile in raw[1:]:
        zeile = zeile.replace(" ", "").replace("$", "").split(",")
        zeile[0] = f"{zeile[0][3:5]}.{zeile[0][:2]}.{zeile[0][6:]}"
        eintrag = {header[0]: zeile[0]}
        for i, key in enumerate(header[1:], start=1):
            eintrag[key] = float(zeile[i])
        result.append(eintrag)
    return result

def write_quotes(target, data, encoding="utf-8"):
    with open(target, "w", encoding=encoding) as file:
        file.write(pprint.pformat(data))
        file.flush()


if __name__ == "__main__":
    import pprint
    # Testbreich bzw. für standalone Einsatz
    FNAME = "/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv"
    raw = read_quotes(FNAME)
    quotes = prepare_quotes(raw)
    df = pandas.DataFrame(quotes)
    print(df)
    print(df["Volume"].values)
    df.to_excel("Test.xls")
    write_quotes("Ergebnis.txt", quotes)
