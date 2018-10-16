""" 
Длина Московской кольцевой автомобильной дороги - 109 километров. Стартуем с нулевого километра МКАД и едем со скоростью V километров в час. На какой отметке остановимся через T часов? Программа получает на вход значение V и T. Если V>0, то движемся в положительном направлении по МКАД, если же значение V<0, то в отрицательном. Программа должна вывести целое число от 0 до 108 - номер отметки, на которой остановимся
"""

speed = int(input('Введите скорость движения, км/ч. '))
time = int(input('Введите время движения, ч. '))
circle_length = 109

if speed > 0:    
    number_of_circle = (speed*time)/circle_length
    stop_point = round(circle_length * (number_of_circle - int(number_of_circle)))
else:
    number_of_circle = (speed*time)/circle_length
    stop_point = circle_length - abs(round(circle_length * (number_of_circle - int(number_of_circle))))

print("Вы остановились на" + " " + str(stop_point) + " " + "км.")



