#! /usr/bin/env python3

import pprint

dict_example ={}

dict_example["Name"] = "Julian"

pprint.pprint(dict_example)


d = {"Name": "Julian", "Age": 30, "Height / cm": 181.1}

werte_k = ["Name","Age","Height / cm"]
werte_v = ["Julian", 30, 181.1]

d2 = {k:v for k in werte_k for v in werte_v}

pprint.pprint(d2)

a = {table: chr(table) for table in range(32, 128)}

pprint.pprint(a)


# werte = range(1,11)
# gw = 5
# l = [n for n in werte if n > gw]

# print(*[x**2 for x in range(1,100)])

# print("test")
# print(*l)


numbers = range(1,11)
# returns True if number is even
def check_even(number):
    if number % 2 == 0:
        return True
    return False

# Extract elements from the numbers list for which check_even() returns True
even_numbers_iterator = filter(check_even, numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)

# Output: [2, 4, 6, 8, 10]


# Maps

l = range(1,6)
quadrate = map(lambda x: x ** 2, l)


l1 = ["a","b","c"]
l2 = [1,2,3]

[list(n) for n in zip(l1,l2)]


