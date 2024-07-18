def month_to_season(print_season):
    print('Время года ' + print_season)  

        
print('Введите номер месяца. Например, январь - 1, февраль - 2 и т.д. ')
month = input()
month = int(month)

if month < 3 and month == 12: month_to_season("Зима")
else:
    if month > 2 and month < 6: month_to_season("Весна")
    else:
        if month > 5 and month < 9: month_to_season("Лето")
        else:
            if month > 8 and month < 12: month_to_season("Осень")
            else: print('Месяца с таким номером не существует')
