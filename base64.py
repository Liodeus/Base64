#!/bin/usr/env Python3
# -*- encoding:utf_8 -*-

import Base64Table

t = "sure."
liste = []
for letter in t:
    test = bin(ord(letter))[2:]

    if len(test) != 8:
        diff = 8 - len(test)

        for i in range(0, diff):
            test = "0" + test

    liste.append(test)


liste2 = []
fullString = "".join(liste)

# Found -> https://gist.github.com/bellbind/255287
te = (fullString[i:i + 6] for i in range(0, len(fullString), 6))

l = ""
s2 = ""
for t in te:
    if len(t) != 6:
        size = 6 - len(t)
        for o in range(0, size):
            t += '0'
    s2 += t
    l += Base64Table.dictio[t]

if (len(s2) + 6) % 24 == 0:
    l += "="
elif (len(s2) + 12) % 24 == 0:
    l += "=="

print(l)
