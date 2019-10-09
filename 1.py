k = int(input('Введи кол-во секунд: '))
h = k / 3600
k %= 3600
m = k / 60
k %= 60
time = '%i:%i:%i' % (h, m, k)
print(time)
