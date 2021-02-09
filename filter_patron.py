import sys

lines = sys.stdin.read().splitlines()

for line in lines:
    line_split = line.split(' ')
    if "np" in line_split:
        print(line)
    if len(line_split) >= 4 and "nc" in line_split:
        print(line)
