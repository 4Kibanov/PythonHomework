my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def a(list, n = 0):
	print(list[n])
	if n + 1 < len(list):
		a(list, n + 1)
	else: print('Конец списка')
	return a

a(my_list)
input('Нажмите Enter для выхода из программы.')
