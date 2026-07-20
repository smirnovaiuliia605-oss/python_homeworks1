from math import ceil


def square(side):
    return ceil(side * side)


side = float(input('Введите сторону квадрата:'))


print(f'Округленная в большую сторону площадь - {square(side)}')
