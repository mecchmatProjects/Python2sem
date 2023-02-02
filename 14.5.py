a = int(input('Введіть значення a = '))
b = int(input('Введіть значення b = '))
c = int(input('Введіть значення c = '))
# f = 0
def quadratic_func(a, b, c):
    x1 = 0
    x2 = 0
    try:
        assert( b**2 - 4 * a * c>=0 )
        x1 = (-b - ( b ** 2 - 4 * a * c)**0.5) / ( 2*a )
        x2 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        if x1 != x2:
            return print(x1, x2 , 'Корені рівняння')
        else:
            return print(x1, 'Рівняння має один корінь')
    except AssertionError:
        print('Рівняння не має коренів')

print(quadratic_func(a, b, c))