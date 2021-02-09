#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

lines = sys.stdin.read().splitlines()

n = int(sys.argv[1])

currentLines = ["0\tXX\tXX"] * (2 * n + 1)

end = False
flag = True

entite = {}

f = open("dico_nom_propre.txt", "r")
line = f.readlines()

for l in line:
    word = l.split('\t')[0]
    ent = l.split('\t')[1]
    if word not in entite:
        entite[word] = ""
    entite[word] += ent + " "

for idLine in range(len(lines)):
    for i in range(-n, n + 1, 1):
        if idLine + i >= 0 and idLine + i < len(lines):
            currentLines[i + n] = lines[idLine + i]
            if currentLines[i + n] == "" or end:
                if n + i > n:
                    end = True
                elif n + i < n:
                    for j in range(-n, n + i, 1):
                        currentLines[j + n] = "0\tXX\tXX"
                currentLines[i + n] = "0\tXX\tXX"
        else:
            currentLines[i + n] = "0\tXX\tXX"

    if currentLines[n] == "0\tXX\tXX":
        end = False
        continue

    for i in range(2 * n + 1):
        currentLines[i] = currentLines[i].split("\t")

    """
    if flag:
        if currentLines[n][4] == "O":
            continue
    """
    print(str(idLine) + " , ", end="")

    for i in range(2 * n + 1):
        if i != n:
            print(currentLines[i][1].replace(",", "!VIRGULE") + " , ", end="")
        else:
            print(currentLines[i][1].replace(",", "!VIRGULE") + " , ", end="")

    if currentLines[2][1] in entite and currentLines[2][2] == 'np':
        print(entite[currentLines[2][1]] + " , ", end="")
    else:
        print("" + " , ", end="")

    print('.')
