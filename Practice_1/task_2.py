""" 
Процентная ставка по вкладу состовляет P процентов годовых, которые прибавляются к сумме вклада. Вклад состовляет X рублей Y копеек.Определите размер вклада через год. Программа получает на вход целые числа P,X,Y и должна вывести два числа: величину вклада через год в рублях и копейках. Дробная часть копее отбрасывается.
"""

p = int(input())
x = int(input())
y = int(input())
deposite_before = 100 * x + y
deposite_after = int(deposite_before * (1 + p/100))
print(deposite_after // 100, deposite_after % 100)

