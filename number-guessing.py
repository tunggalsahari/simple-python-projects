# This is a simple number guessing game in python

import random

header = ("=> Input number range you would like to choose.")
example = ("=> Example: use numbers between 1 and 30.")
print(header)
print(example) 

first = int(input("=> Input the first number: "))
second = int(input("=> Input the second number: "))

pick = int(input("=> Input your number of choice: "))
shuffle = random.randrange(first, second)

if shuffle == pick:
    print(f"=> You are correct! The answer is {shuffle}")
else:
    print(f"=> You are wrong! The answer is {shuffle}")
