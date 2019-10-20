import math
import random


def fibo_gen():
    yield math.factorial(random.randint(1, 100))

print(fibo_gen())

for el in fibo_gen():
    print(f'{el}'[1:16])

