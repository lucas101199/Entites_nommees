#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from parse import parse

phrases = parse()

entities = {}
entity = ""
entityLabel = ""

for phrase in phrases:
    for wordInfos in phrase:
        morph = wordInfos[2]
        label = wordInfos[3]
        if "B" in label:
            if len(entity) > 0:
                if entity not in entities.keys():
                    entities[entity] = 0
                entities[entity] += 1
            entity = morph
        elif "I" in label:
            entity += " " + morph
        elif len(entity) > 0:
            if len(entity) > 0:
                if entity not in entities.keys():
                    entities[entity] = 0
                entities[entity] += 1
            entityLabel = ""
            entity = ""
  
entities = dict(sorted(entities.items(),
                        key=lambda item: item[1],
                        reverse=True))

for entity in entities.keys():
    print(entity)
