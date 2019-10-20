import random

my_list = []
rand = int(random.randint(1, 100))
for i in range(rand):
    my_list.append(i)
new_list = [el+11 for el in my_list]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")

