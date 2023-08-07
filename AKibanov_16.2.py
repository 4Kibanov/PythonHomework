class Turtle:
    def __init__(self, x, y, s):
        self.x, self.y, self.s = x, y, s
    
    def go_up(self):
        self.y += self.s
        return self.y

    def go_down(self):
        self.y -= self.s
        return self.y

    def go_left(self):
        self.x -= self.s
        return self.x

    def go_right(self):
        self.x += self.s
        return self.x
    
    def evolve(self):
        self.s += 1
        return self.s
    
    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else: print('Черепашка не может ходить меньше 1')
        return self.s
    
    def count_moves(self, x2, y2):
        return (x2 - self.x)//self.s, (y2 - self.y)//self.s

r=Turtle(2, 2, 2)
#Стартовая позиция x=2, y=2; шаг s=2
print('y=', r.go_up())
print('y=', r.go_down())
print('x=', r.go_left())
print('x=', r.go_right())
print('s=', r.evolve())
print('y=', r.go_up())
print('y=', r.go_up())
print('s=', r.degrade())
print('s=', r.degrade())
print('s=', r.degrade())
#Повышаем шаг с 1 до 2, а потом проверяем, как из текущих x=2 и y=8 добраться до x=2 и y=2
print('s=', r.evolve())
print(r.count_moves(2, 2))
#Получается, что по x нужно 0 шагов, а по y необходимо 3 шага вниз
input('Нажмите Enter для выхода из программы.')