#!/usr/bin/env python3
import sys 

def build_table():
    header = ["   "] + [str(col) for col in range(0,10)]
    table = [header]
    for i in range(30, 130, 10):
        table.append([str(i)] + [chr(i+j) if chr(i+j).isprintable() else "." for j in range(0,10)])
    return table

def print_table(table):
    print("|".join(table[0]))
    for row in table[1:]:
        print(f"{row[0]:<3}|{' '.join(row[1:])}")

if __name__ == "__main__":
    table = build_table()
    print_table(table)
    sys.exit(0)