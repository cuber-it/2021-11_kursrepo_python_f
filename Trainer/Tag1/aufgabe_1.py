#!/usr/bin/env python3
ascii = {chr(n): n for n in range(32, 128)}

line = ""
for i, k in enumerate(ascii.items()):
    if i % 8:
        line += f"{k[0]}:{k[1]:>3} "
    else:
        print(line)
        line = f"{k[0]}:{k[1]:>3} "
print(line)
   
        