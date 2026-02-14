#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        res = "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)

        print("{}".format(res or i), end=" ")
