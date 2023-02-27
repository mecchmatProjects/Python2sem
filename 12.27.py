inventar = {}
with open('f1.txt', 'r') as f1:
    for line in f1:
        line = line.split()
        inventar[line[0]] = int(line[1])
with open('f2.txt', 'r') as f2:
    for line in f2:
        line = line.split()
        inventar[line[0]] = inventar.get(line[0], 0) + int(line[1])
with open('g.txt', 'w') as g:
    for key, value in inventar.items():
        g.write(key + ' ' + str(value) + '\n')