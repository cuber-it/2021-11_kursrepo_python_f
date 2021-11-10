#!/usr/bin/env python3
import pandas

df = pandas.read_csv("/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv")

print(df)
print(df[" Volume"].values)