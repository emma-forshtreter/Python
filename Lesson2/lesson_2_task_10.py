def bank(print_Sum):
    print('На Вашем счету ', end='')
    print(print_Sum)

print('Сумма вклада: ')
X = input()
X = float(X)

print('На сколько лет? ')
Y = input()
Y = float(Y)

bank(X * pow((1 + 0.1),Y))         