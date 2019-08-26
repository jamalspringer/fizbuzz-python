#!/usr/bin/python

print "Welcome to Fizzbuzz"


def fizzbuzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"

