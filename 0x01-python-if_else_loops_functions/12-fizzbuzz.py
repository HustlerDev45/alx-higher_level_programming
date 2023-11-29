#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("{0}".format("FizzBuzz"), end=' ')
        elif n % 3 == 0:
            print("{0}".format("Fizz"), end=' ')
        elif n % 5 == 0:
            print("{0}".format("Buzz"), end=' ')
        else:
            print("{0}".format(n), end=' ')
    print()
