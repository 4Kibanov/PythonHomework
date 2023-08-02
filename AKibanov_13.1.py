import random
random.seed()
def pl(t):
	for i in t:
		print(*i)

def Matrix():
	print('Введите значения x и y через Enter для размера матрицы (например, 4х3): ')
	x = int(input())
	y = int(input())
	matrix = []
	for i in range(x):
		matrix.append([])
		for j in range(y):
			matrix[i].append(random.randint(-100, 100))
	return matrix

def sumMatrix(a, b):
	matrix = []
	for i in range(len(a)):
		matrix.append([])
		for j in range(len(a[i])):
			matrix[i].append(a[i][j] + b[i][j])
	return matrix

A, B = Matrix(), Matrix()
print('Значения внутри матриц сгенерированы случайно в диапазоне от -100 до 100: ')
print('Первая матрица: ')
pl(A)
print('Вторая матрица: ')
pl(B)
print('Сумма матриц: ')
pl(sumMatrix(A, B))
input('Нажмите Enter для выхода из программы.')