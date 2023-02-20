defaultdict = {(i, i + 1): i + 100 for i in range(10)}

# г
# максимальний елемент розрідженої матриці
max_num = max(defaultdict.values())
print(max_num)

# д
defaultdict['ВЕКТОР'] = 5
for key, value in defaultdict.items():
    defaultdict[key] *= defaultdict['ВЕКТОР']
print(defaultdict)

# e
# якщо i < j, це означає що елемент знаходиться вище головної діагоналі
# відповідно він є ненульовим і відповідно матриця не є нижньою трикутною
for key in defaultdict.keys():
    if key[0] < key[1]:
        print('матриця не є нижньою трикутною')
        break
    else:
        print('матриця є нижньою трикутною')


