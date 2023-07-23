x = int(input('Введите количеcтво строк массива: '))
if x < 1 or x > 10000:
  print('Количество строк массива не должно быть меньше 1 или больше 10000!')
  exit()
print('Введите числа массива через Enter для каждой строки: ')
N = []
for i in range(x):
    N.append(int(input()))
N.reverse()
print(N)
input('Нажмите Enter для выхода из программы.')
