import pprint

fname = "/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv"

def read_quotes(fname):
    with open(fname) as fd:
        return fd.read().splitlines()

def prepare_quotes(values):
    result = []
    header = values[0].split(",")
    for row in values[1:]:
        row = row.split(",")
        entry = {}
        for i, key in enumerate(header):
            if key == "Date":
                entry[key] = f"{row[i][3:5]}.{row[i][0:2]}.{row[i][6:]}"
            else:
                entry[key] = float(row[i].replace("$",""))
            
        result.append(entry)
    return result

if __name__ == "__main__":
    raw = read_quotes(fname)
    quotes = prepare_quotes(raw)
    pprint.pprint(quotes)