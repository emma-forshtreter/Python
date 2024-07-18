print('Введите любое целое положительное число: ', end="")
number = input()
number = int(number) + 1
def fizz_buzz(n):
    for n in range (1, number):
        if (n % 3 == 0) and (n % 5 == 0): print('FizzBuzz')
        else:
            if n % 5 == 0: print('Buzz')
            else:
                if n % 3 == 0: print('Fizz')
                else:
                    print(n)
fizz_buzz(number)   