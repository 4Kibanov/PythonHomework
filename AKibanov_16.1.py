class Cassa:
    def __init__(self):
        self.count = 0

    def top_up(self, x):
        self.count += x
        print(self.count)
	
    def count_1000(self):
        return int(self.count / 1000)

    def take_away(self, x):
        if self.count > x:
            self.count -= x
            print(self.count)
        else: print('Недостаточно денег в кассе!')

cassa = Cassa()
#Пополняем кассу на 12345 единиц валюты
cassa.top_up(12345)
#Проверяем сколько целых тысяч единиц в кассе
print(cassa.count_1000())
#Забираем из кассы 6789 единиц валюты
cassa.take_away(6789)
#Пробуем взять из кассы 6000 единиц валюты
cassa.take_away(6000)
input('Нажмите Enter для выхода из программы.')