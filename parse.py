#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def parse():

    import sys
    
    phrases = []
    phrase = []
    
    for line in sys.stdin.read().splitlines():
        infos = line.split("\t")
        if len(infos) != 4:
            phrases.append(phrase.copy())
            phrase = []
        elif len(phrase) == 0:
            phrase.append(infos.copy())
        else:
            phrase.append(infos.copy())
                
    return phrases