#!/usr/bin/python3

""" Ремонт в квартире 

Есть квартира (2 комнаты и кухня). В квартире планируется ремонт: нужно 
поклеить обои, покрасить потолки и положить пол.

Необходимо рассчитать стоимость материалов для ремонта.

Из описания следуют следующие классы:
= Строительные материалы
  = Обои
  = Потолочная краска
  = Ламинат
= Комната
= Квартира

Подробнее, с методами (+) и атрибутами (-):
= Строительные материалы
  - площадь (кв. м)
  - цена за единицу (рулон, банку, упаковку)
  = Обои
    - ширина рулона
    - длина рулона
  = Потолочная краска
    - вес банки
    - расход краски
  = Ламинат
    - длина доски
    - ширина доски
    - кол-во досок в упаковке
= Комната
  - ширина
  - высота
  - длина
  - ширина окна
  - ширина двери
  + поклеить обои
  + покрасить потолок
  + положить пол
  + посчитать смету на комнату
  + при создании комнаты сразу передавать все атрибуты в конструктор __init__()
= Квартира
  - комнаты
  + добавить комнату
  + удалить комнату
  + посчитать смету на всю квартиру
  + при создании можно передать сразу все комнаты в конструктор

Необходимо создать стройматериалы, назначить им цены и размеры.
Создать комнаты, поклеить, покрасить и положить все на свои места.
Cоздать квартиру, присвоить ей комнаты и посчитать общую смету.

Подсказка: для округления вверх и вниз используйте:
import math
math.ceil(4.2)  # 5
math.floor(4.2) # 4

Примечание: Для простоты, будем считать, что обои над окном и над дверью 
не наклеиваются.
----------------

Дополнительно:
Сделать у объекта квартиры метод, выводящий результат в виде сметы:

[Комната: ширина: 3 м, длина: 5 м, высота: 2.4 м]
Обои        400x6=2400 руб.
Краска     1000x1=1000 руб.
Ламинат     800x8=6400 руб.
[Комната: ширина: 3 м, длина: 4 м, высота: 2.4 м]
Обои        400x5=2000 руб.
Краска     1000x1=1000 руб.
Ламинат     800x7=5600 руб.
[Кухня: ширина: 3 м, длина: 3 м, высота: 2.4 м]
Обои        400x4=1600 руб.
Краска     1000x1=1000 руб.
Ламинат     800x5=4000 руб.
---------------------------
Итого: 25000 руб.

"""
import math
class Room ():
    def __init__(self,l,w,h,win = 1.2,door = 1):
        self.l = l
        self.h = h
        self.w = w
        self.win = win
        self.door = door
    def floor(self,lam):
        pl = self.l*self.w
        q = pl/lam.ss()
        return (q)
    def param(self):
        return ([self.l,self.w,self.h])
    def walls (self,wp):
        per = (self.l+self.w)*2-self.win - self.door
        pl = per * self.h
        return (pl/wp.ss())
    def ceil(self,pn):
        return (self.l*self.w/pn.ss())
    def countr(self, wp,pn,lam):
        oboi = (wp.pr(),math.ceil(self.walls(wp)),math.ceil(self.walls(wp))*wp.pr())
        kraska = (pn.pr(),math.ceil(self.ceil(pn)),math.ceil(self.ceil(pn))*pn.pr())
        laminat = (lam.pr(),math.ceil(self.floor(lam)),math.ceil(self.floor(lam))*lam.pr())
        #print (l1)
        return (oboi,kraska,laminat)
    
class Material():
    def __init__(self,s,price):
        self.s = s
        self.price = price
class Wallpaper(Material):
    def __init__(self,s, price, l, w):
        super().__init__(s,price)
        self.l = l
        self.w = w
    def pr(self):
        return (self.price)
    def ss(self):
        return (self.l*self.w)# сколько один рулон покрывает стен
class Laminat(Material):
    def __init__(self,s, price, l, w,n):
        super().__init__(s,price)
        self.l = l
        self.w = w
        self.n = n
    def ss(self):
        return (self.l*self.w*self.n)# сколько одна упаковка покрывает пола
    def pr(self):
        return (self.price)
class Paint(Material):
    def __init__(self,s, price, weight, cons):
        super().__init__(s,price)
        self.weight = weight # в кг
        self.cons = cons #кг на кв.м
    def ss(self):
        return (self.weight/self.cons) #сколько одной баанкой можно покрасить кв.м.
    def pr(self):
        return (self.price)
class Flat():
    def __init__(self):
        self.myflat=[]
    def add(self,room):
        self.myflat.append(room)
    def rem(self,room):
        self.myflat.remove(room)
        
    def countf(self):
        smeta=0
        for i in self.myflat:
            for j in range(3):
                smeta += i.countr(wp,pp,lam1)[j][2]
        return (smeta)
    def show(self):
        return (self.myflat)
        
wp = Wallpaper(1,2000,10,0.5)
lam1=Laminat(1,1200,1.2,0.2,6)
pp = Paint(1,5000,5,0.25)
myroom = Room (4, 5, 2.5, 1.5,1)
mr = Room (5, 3, 2.5, 1.5,1)
mr1 = Room (4.1, 3.5, 2.5, 1,0.9)

#g = myroom.countr(wp,pp,lam1)

f = Flat()
f.add(myroom)
f.add(mr)
f.add(mr1)
#print (f.countf())
print ('Смета на квартиру:')
for i in f.show():
    print ("-"*30)
    print ('[Комната: длина = {} м, ширина = {} м, высота ={} м]'.format(i.param()[0],i.param()[1],i.param()[2]))
    rr = i.countr(wp,pp,lam1)
    print ('Обои     {:5} * {:2} = {:6} руб'.format(rr[0][0],rr[0][1],rr[0][2]))
    print ('Краска   {:5} * {:2} = {:6} руб'.format(rr[1][0],rr[1][1],rr[1][2]))
    print ('Ламинат  {:5} * {:2} = {:6} руб'.format(rr[2][0],rr[2][1],rr[2][2]))
print ("="*30)
print ('ИТОГО:   {} руб.'.format(f.countf()))
