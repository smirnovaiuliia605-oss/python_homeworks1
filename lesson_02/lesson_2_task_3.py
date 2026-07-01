from math import ceil


def ceil_sum(a, b):
    return ceil(a + b)


a = float(input('Введите первое слагаемое:'))
b = float(input('Введите второе слагаемое:'))


print(f'Округленная в большую сторону сумма - {ceil_sum(a, b)}')
