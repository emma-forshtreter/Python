#def bank(print_Sum):
#    print('На Вашем счете: ', end='')
#    print(print_Sum)
#
#print('Сумма вклада: ')
#X = input()
#X = float(X)
#
#print('На сколько лет? ')
#Y = input()
#Y = float(Y)
#
#bank(X * pow((1 + 0.1),Y))   

X = float(input('Сумма вклада: '))
Y = int(input('На сколько лет? '))

def bank(X,Y):                     
    for i in range(Y):
        X = X + (X * 0.1)          # 0.1 = 10%
    return print(round(X,1))
print(bank(X,Y))