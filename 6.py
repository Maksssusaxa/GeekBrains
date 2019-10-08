# from itertools import count # Бесконечный итератор чисел
# from itertools import cycle

# for i in count(1):
#   print(i)

polys = ['triangle', 'square', 'pentagon', 'rectangle'] # бесконечный итератор значений списка
for i in cycle(polys):
    print(i)


