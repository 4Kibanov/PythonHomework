x, y = list(map(int, input('Введите через пробел диапазон двух чисел (например, 10 -5): ').split()))
my_dict = {}
s1, s2 = x, y
step = s2 - s1
if step < 0: step = -1
else: step = 1

for i in range(s1, s2 + step, step):
    my_dict[i] = i ** i
print(my_dict)
input('Нажмите Enter для выхода из программы.')