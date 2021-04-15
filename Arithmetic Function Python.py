# -*- coding: utf-8 -*-
"""Arithmetic Function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xh2HuFaR3f8_SxrHg9tORm1_j2_VegJe

# Functional Programming
---

## Arithmetic Function
"""

def addition():
    a = 50
    b = 20
    total = a + b
    print('Total is :', total)

addition()

"""## Arithmetic Function with Parameters"""

def multiplicationn(a, b):
    print('Total is :', a * b)

multiplication(a=40, b=30)

"""## Arithmetic Function with Parameters and Output"""

def divide(a, b, c=2):
    total = a * b / c
    return total

result = divide(10, 5)
print(result)

"""## Function with Conditional Statement"""

def wealth_estimator(money):
    if money >= 1000000:
        status = 'You are rich'

    elif money < 1000000 and money <= 100:
        status = 'You are in middle class'

    else:
        status = 'You are poor'

    return status

status = wealth_estimator(2000)
print(status)

"""## Function with Loop"""

numbers = [1, 2, 3, 4, 5]

def add_number(array, extra=2):
    placeholder = []

    for number in array:
        new_number = number + extra
        placeholder.append(new_number)

    return placeholder

result = add_number(numbers, extra=10)

"""## Function inside Function"""

def multiplication(a, b):
    return a * b

def multiply_number(array, extra=2):
    placeholder = []

    for number in array:
        new_number = multiplication(number, extra)
        placeholder.append(new_number)

    return placeholder

numbers = [1, 2, 3, 4, 5]
result = multiply_number(numbers, extra=10)

"""# String Manipulation

## Concatenate
"""

message = 'hello' + ' ' + 'world'
print(message)

"""## Multiply"""

star = '*' * 3
message_ = 'hello ' * 3
message_1 = 'world'
print(star + message_ + message_1+ star)

"""## Length"""

messagep = 'ksdfjdsbhvciusd sdhbfsdkfkhsbdfkds skufksdhufbsdbfkshfhsd subfdsubfoubosdufg  ashdfaoudsfasudfioasdfiu asudfaisudbfasdfsu'
if len(messagep) > 20:
    print('too long!')
else:
    print('okay')

"""## Lower case, Upper case, Capitalize"""

# Lower Case
message7 = "HELLO WORLD"
message7a = message7.lower()
print(message7a)

# Upper Case
message7a = message7.upper()
print(message7a)

# Capitalize
message7a = message7.capitalize()
print(message7a)

"""## Replace"""

message8 = "HELLO WORLD"
message8a = message8.replace("L", "chicken")
print(message8a)

"""## Slice"""

message9 = "Hello World"
message9a = message9[1:7]
print(message9a)