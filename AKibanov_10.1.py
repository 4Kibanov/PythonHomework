﻿print('Добро пожаловать на сайт нашей ветеринарной клиники')
name = input('Введите имя вашего питомца: ')
breed = input('Пожалуйста, введите вид вашего питомца: ')
age = int(input('Укажите возраст вашего питомца: '))
owner = input('Введите имя владельца: ')
pets = {
    "Имя питомца": name,
    "Вид питомца": breed,
    "Возраст питомца": age,
    "Имя владельца": owner
    }

#Проверка что питомец появился в словаре
name = pets["Имя питомца"]
breed = pets["Вид питомца"]
age = pets["Возраст питомца"]
owner = pets["Имя владельца"]
years = 'лет'
if age < 5 or age > 20:
    x = age % 10
    if x == 1: years = 'год'
    elif x < 5: years = 'года'
print(f'Это {breed} по кличке "{name}". Возраст питомца: {age} {years}. Имя владельца: {owner}')
input('Нажмите Enter для выхода из программы.')