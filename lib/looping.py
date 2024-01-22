#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        if i == 1:
            print('Happy New Year!')
        i -= 1

def square_integers(int_list):
    squared_list = []
    for num in int_list:
        squared_list.append(num * num)
    return squared_list

def fizzbuzz():
    i = 1
    while i < 101:
        if (i / 3).is_integer() and (i / 5).is_integer():
            print("FizzBuzz")
            i += 1
        elif (i / 3).is_integer():
            print("Fizz")
            i += 1
        elif (i / 5).is_integer():
            print("Buzz")
            i += 1
        else:
            print(i)
            i += 1
        
