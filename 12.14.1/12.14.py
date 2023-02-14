with open('h.txt', 'w') as h:
    with open('f1.txt', 'r') as f1:
        h.write(f1.read())
with open('f2.txt', 'r') as f2:
    with open('f1.txt', 'w') as f1:
        f1.write(f2.read())
with open('f2.txt', 'w') as f2:
    with open('h.txt', 'r') as h:
        f2.write(h.read())