def _12_24():
    '''12.24.Дано файл, який містить відомості про кубики: розмір кожного  кубику  (довжина  ребра  в  см),  його  колір  (червоний, жовтий,  зелений,  синій)  та  матеріал  (дерев'яний,  металевий, картонний). Скласти процедури пошуку
    а)  кількості  кубиків  кожного  з  перелічених  кольорів  та  їх сумарний об'єм;
    б) кількості дерев'яних кубиків із ребром 3 см та кількості металевих кубиків з ребром більшим за 5 см.'''
    try:
        with open('data.txt', 'r') as f:
            data = f.readlines()
    except FileNotFoundError:
        data = '''3, green, wood
5, green, metal
2, red, wood
4, green, metal
3, green, wood
7, green, metal
5, blue, cardboard
5, green, metal
4.3, red, metal
3, green, wood
'''.splitlines()
    cubes = []

    for i in data:
        cube = i.split(',')
        size = float(cube[0])
        color = cube[1].strip()
        material = cube[2].strip()

        cubes.append((size, color, material))

    print(cubes)

    _colored = {}

    for cube in cubes:
        color = _colored.get(cube[1], [])
        color.append(cube)
        _colored[cube[1]] = color

    print(_colored)

    colored = {}
    for k, v in _colored.items():
        colored[k] = (len(v), sum(map(lambda x: x[0], v)))
    print(colored)

    counter = {}
    for cube in cubes:
        if cube[0] == 3 and cube[2] == 'wood':
            counter['wood'] = counter.get('wood', 0) + 1
        if cube[0] == 5 and cube[2] == 'metal':
            counter['metal'] = counter.get('metal', 0) + 1
    print(counter)

if __name__ = '__main__':
    _12_24()
