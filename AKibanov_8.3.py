﻿m = int(input('Введите максимальную массу, которую может выдержать одна лодка: '))
if m < 1 or m > 10e6:
  print('Масса для лодки не должна быть меньше 1 или больше 1000000!')
  exit()
n = int(input('Введите колличество рыбаков (в 1 лодку помещается не более 2 человек): '))
if n < 1 or n > 100:
  print('Количество рыбаков не должно быть меньше 1 или больше 100!')
  exit()
print('Введите вес каждого рыбака через Enter: ')
N = []
count = 0

for i in range(n):
    N.append(int(input()))
N.sort()
while N:
    if (N[0] + N[-1]) > m:
        count += 1
        N.pop()
    elif len(N) > 1:
        N.pop()
        N.pop(0)
        count += 1
    else:
        N.pop()
        count += 1
print('Количество необходимых лодок, для перевозки рыбаков:', count)
input('Нажмите Enter для выхода из программы.')
