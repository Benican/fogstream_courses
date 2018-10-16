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


