#!/usr/bin/env python3
def mach_was(x):
    return f"Hey {x}"


def tu_was(x):
    return f"Huhu {x}"

jt = {
    "A": mach_was,
    "B": tu_was,
    "C": tu_was,
    "D": lambda x: f"--{x}--"
}



for x in ["B", "A", "C", "C", "D"]:
    print(jt[x](x))