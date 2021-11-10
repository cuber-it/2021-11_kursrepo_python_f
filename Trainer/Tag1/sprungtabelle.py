import stockquotes

def faktor10(x):
    return(x * 10)

jump_table = {
    "High": faktor10,
    "Low" : lambda x: x * 5,
    "Open": lambda x: "|" + str(x) + "|",
    #"Volume": lambda x: len(str(x))
}


def main():
    aapl = stockquotes.Quotes("AAPL", "/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv").read() # Initialisierung
    for row in aapl.to_dict():
        for k, v in row.items():
            if k in jump_table:
                print(k, jump_table[k](v))
            else:
                print(k, v)

main()
