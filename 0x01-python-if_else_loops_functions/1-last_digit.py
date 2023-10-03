#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_s = str(number)
number_i=int(number_s[-1])
if number_i > 5:
    print(f"Last digit of {number} is {number_i} and is greater than 5")
elif number_i < 6 and number_i != 0:
    print(f"Last digit of {number} is {number_i} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {number_i} and is 0")
