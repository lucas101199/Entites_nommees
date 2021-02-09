import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
data = open("corpus_500.train.data", "w")
dev = open("corpus_500.train.dev", "w")

for i in range(0, len(lines)-1):
    if i < len(lines) * 0.7:
        data.write(lines[i])
    else:
        dev.write(lines[i])
