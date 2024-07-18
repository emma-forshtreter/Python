is_year_leap = input('Введите любой год в формате ГГГГ: ')
print('Вы ввели: ' + is_year_leap)

is_year_leap = int(is_year_leap)

if (is_year_leap % 4 == 0):
    print('Год ', end="")
    print(is_year_leap, end="")
    print(': True', end="")
else: 
    print('Год ', end="")
    print(is_year_leap, end="")
    print(': False')