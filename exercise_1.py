a =int(input('введите число очков игрока в боулинге'))
k = a
while a != -1:
    a = int(input('введите число очков игрока в боулинге'))
    if k < a:
        k = a
print(k)