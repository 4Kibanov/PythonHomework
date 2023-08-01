#Нахождение факториала рекурсией
def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n

def Factorial_list(x):
    list = []
    n = fac(x)
    for i in range(n, 0, -1):
        list.append(fac(i))
    print(f'Список из факториалов получившегося числа {n}: ', list)
Factorial_list(int(input("Введите число, чтобы получить его факториал (например, 3): ")))
input('Нажмите Enter для выхода из программы.')