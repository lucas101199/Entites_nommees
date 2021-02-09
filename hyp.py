#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

f = open(sys.argv[1])
lines = f.read().splitlines()
f.close()

patrons = []
for line in lines:
    patrons.append(line.split(" "))

lengthMax = max(len(patron) for patron in patrons)

arbre = {}
for patron in patrons:
    noeud = arbre
    for pos in patron:
        if pos not in noeud.keys():
            if pos != patron[-1]:
                noeud[pos] = {}
            else:
                noeud[pos] ={None:None}
        noeud = noeud[pos]

lines = sys.stdin.read().splitlines().copy()
hyp = ["O"]*len(lines)

idLine = 0
while idLine <len(lines):
    infos = lines[idLine].split("\t")
    if len(infos) != 4:
        hyp[idLine] = ""
        idLine += 1
        continue
    patron = []
    patron.append(infos[2])
    noeud = arbre
    found = False
    i = 1
    while patron[-1] in noeud.keys():
        noeud = noeud[patron[-1]]
        if None in noeud.keys():
            found = True
            break
        if idLine+i >= len(lines):
            break
        infos = lines[idLine+i].split("\t")
        if len(infos) != 4:
            break
        patron.append(infos[2])
        i += 1
    if found:
        for j in range(0,i):
            if hyp[idLine+j] != "hyp":
                hyp[idLine+j] = "hyp"
    idLine += 1

for i in range(0,len(lines)):
    if hyp[i] != "":
        print(lines[i] + "\t" + hyp[i])
    else:
        print(lines[i])
    
