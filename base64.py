#!/bin/usr/env Python3
# -*- encoding:utf_8 -*-


t = "Hi!"
liste = []
for letter in t:
    test = bin(ord(letter))[2:]

    if len(test) != 8:
        diff = 8 - len(test)

        for i in range(0, diff):
            test = "0" + test

    liste.append(test)

print("".join(liste))
