from itertools import groupby
import random
x = []
rand = int(random.randint(1, 100))
for i in range(rand):
    x.append(i)
    x.append(i)
new_x = [el for el, _ in groupby(x)]
print(x)
print(new_x)

