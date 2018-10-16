interest_rate = int(input('Введите годовую ставку процента, %. '))
bank_deposite = input('Введите размер банковского вклада, руб.коп ').split(".")

rub = int(bank_deposite[0])
cent = int(bank_deposite[1])

bank_deposite_total = ((rub*100+cent)*(1+interest_rate/100))/100
rub = int(bank_deposite_total)
cent = round(100*(bank_deposite_total-int(bank_deposite_total)))

print('Ваш банковский депозит равен' + ' ' + str(rub) + ' ' + 'рублей' + ' ' +str(cent) + ' '+ 'копеек')





