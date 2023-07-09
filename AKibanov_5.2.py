x = input('Введите английское слово маленькими буквами: ')
vowels = ['a', 'e', 'i', 'o', 'u']
a = 0
b = 0
print('Количество для каждой гласной буквы:')
for str in vowels:
    if str in x:
        count = x.count(str)
        print(f'{str}: {count}')
        a += count
    else: 
        print(f'{str}: False')
b = len(x) - a
print(f'Количество согласных букв: {b}\n' f'Количество гласных букв: {a}.')
input('Нажмите Enter для выхода из программы.')
