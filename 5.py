import random
list = []
rand = random.randint(1, 100)
for i in range(rand):
    x = random.randint(100, 1001)
    if x // 2 == x / 2:
        list.append(x)
    else:
        continue
new_list = sum(list)
print(new_list)

