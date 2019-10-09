a = int(input('Введи начальный результат: '))
b = int(input('Введи конечный результат: '))
c = a
score = 0
while a < b:
    a = c / 100 * 10 + a
    score += 1
print(score)


