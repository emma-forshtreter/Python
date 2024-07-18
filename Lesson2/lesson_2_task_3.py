print('Введите сторону квадрата: ')
side = input()
side = int(side)
def square(print_square):
    print('Площадь квадрата со стороной ', end="")
    print(side, end="")
    print(' равна ', end="")
    print(print_square, end="")
square(side * side)