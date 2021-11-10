#import stockquotes

from stockquotes import Quotes as Q

def main():
    aapl = Q("AAPL", "/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv") # Initialisierung
    print(type(aapl))

    aapl.read() # Nutzung
    aapl.write("Testdaten", "CSV")
    #print(aapl.to_dict())
    print(aapl.stockname)


main()