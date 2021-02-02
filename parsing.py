from collections import defaultdict

f = open("corpus_en_200k.train.txt", "r")

lines = f.readlines()
entites = {}
ambiguity = defaultdict(list)

for line in lines:
    if len(line.split('\t')) == 4:
        name_entite = line.split('\t')[3][:-1]
        word = line.split('\t')[1]
        if name_entite in entites:
            entites[name_entite] += 1
        else:
            entites[name_entite] = 0

        if word in ambiguity:
            if name_entite not in ambiguity[word]:
                ambiguity[word].append(name_entite)
        else:
            ambiguity[word].append(name_entite)

# number entities of each type
entites_sorted = sorted(entites.items(), key=lambda item: item[1])
# print(entites_sorted)

for k, v in ambiguity.items():
    if len(v) <= 1:
        ambiguity.pop(k)


def sort_by_values_len(dict):
    dict_len = {key: len(value) for key, value in dict.items()}
    import operator
    sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1), reverse=True)
    sorted_dict = [{item[0]: dict[item[0]]} for item in sorted_key_list]
    return sorted_dict


print(sort_by_values_len(ambiguity))
