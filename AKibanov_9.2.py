c1 = int(input('Введите количество чисел для первого массива: '))
print('Введите числа первого массива через Enter: ')
cl1 = []
for i in range(c1):
    name = int(input())
    cl1.append(name)
uc1 = set(cl1)

c2 = int(input('Введите количество чисел для второго массива: '))
print('Введите числа второго массива через Enter: ')
cl2 = []
for i in range(c2):
    name = int(input())
    cl2.append(name)
uc2 = set(cl2)

print('Количество одинаковых чисел в двух массивах:', len(uc1 & uc2))
input('Нажмите Enter для выхода из программы.')
