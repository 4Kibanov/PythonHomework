print('Введите последовательность чисел через пробел, чтобы узнать повторяются числа или нет: ')
a = list(map(int, input().split()))
set1 = set()
for x in (a):
    if x in set1:
        print(f'{x}: YES')
    else:
        set1.add(x)
        print(f'{x}: NO')
input('Нажмите Enter для выхода из программы.')