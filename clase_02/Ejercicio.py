from functools import reduce
import math

_break = ""
_jump = "\n"

print(f'* * * EXERCISE 1 * * *{_break}')


def exercise1():
    var = 'Hola Mundo'
    print(f'response = {var}')


exercise1()
print(f'{_jump}')

print(f'* * * EXERCISE 2 * * *{_break}')


def exercise2(hours, unitary):
    total = hours * unitary
    print(f'total = {total}')


in_hours = int(input('hours: '))
in_unitary = int(input('unitary: '))

exercise2(in_hours, in_unitary)
print(f'{_jump}')

print(f'* * * EXERCISE 3 * * *{_break}')


def exercise3(quantity):
    normal = 1200
    discount = 60
    discounted = int(normal * discount / 100)
    print(f'normal price = {normal} - discount = {discount}% => discounted price = {discounted}')
    print(f'quantity = {quantity}')
    normal = quantity * normal
    discounted = int(quantity * discounted)
    print(f'total normal price = {normal} => total discounted price = {discounted}')


in_quantity = int(input('quantity: '))

exercise3(in_quantity)
print(f'{_jump}')

print(f'* * * EXERCISE 4 * * *{_break}')


def exercise4(salary):
    if salary <= 200000:
        increment = 15
    else:
        increment = 10
    total = int(salary + salary * increment / 100)
    print(f'salary = {salary} + increment = {increment}% => total = {total}')


in_salary = int(input('salary: '))

exercise4(in_salary)
print(f'{_jump}')

print(f'* * * EXERCISE 5 * * *{_break}')


def exercise5(present, rate, periods):
    offset = 1 + rate / 100
    future = present * math.pow(offset, int(periods))
    print(f'present = {present} => future = {future:.2f}')


in_present = int(input('present: '))
in_rate = int(input('rate: '))
in_periods = int(input('periods: '))

exercise5(in_present, in_rate, in_periods)
print(f'{_jump}')

print(f'* * * EXERCISE 6 * * *{_break}')


def exercise6(number):
    total = number * 10
    print(f'total = {total}')


in_number = int(input('number: '))

exercise6(in_number)
print(f'{_jump}')

print(f'* * * EXERCISE 7 * * *{_break}')


def exercise7(height, width):
    for offset_y in range(0, height):
        for offset_x in range(0, width):
            print('*', end='')
        print('')


in_height = int(input('height: '))
in_width = int(input('width: '))

exercise7(in_height, in_width)
print(f'{_jump}')

print(f'* * * EXERCISE 8 * * *{_break}')


def addition(array):
    total = 0
    for offset in array:
        total += offset
    print(f'addition = {total}')


def production(array):
    total = 1
    for offset in array:
        total *= offset
    print(f'production = {total}')


def exercise8(value1, value2, value3):
    array = [value1, value2, value3]
    addition(array)
    production(array)


in_value1 = int(input('value 1: '))
in_value2 = int(input('value 2: '))
in_value3 = int(input('value 3: '))

exercise8(in_value1, in_value2, in_value3)
print(f'{_jump}')

print(f'* * * EXERCISE 9 * * *{_break}')


def concatenation(array):
    string = reduce(lambda offset_1, offset_2: str(offset_1) + str(offset_2), array)
    print(f'concatenation = {string}')


def exercise9(value1, value2, value3):
    array = [value1, value2, value3]
    concatenation(array)


in_value1 = int(input('value 1: '))
in_value2 = int(input('value 2: '))
in_value3 = int(input('value 3: '))

exercise9(in_value1, in_value2, in_value3)
