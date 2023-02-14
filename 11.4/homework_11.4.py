group = [['name' + str(j) for j in range(i, i + 3)] for i in range(1, 4)]
print(group)
top_guests = set(group[0])
for x in group:
    top_guests = top_guests.intersection(set(x))
print(top_guests)