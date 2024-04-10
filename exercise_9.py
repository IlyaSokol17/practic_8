N = int(input('введите число: '))
for t in range(2, N):
    s = 0
    for i in range(1, t + 1):
        n = t / i
        if n == int(n):
            s += n
    if s == t + 1:
        print(t)

