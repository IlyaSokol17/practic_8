N = int(input('введите число: '))
for t in range(2, N):
    a = t
    s = 0
    for i in range(2, a + 1):
        n = a / i
        if n == int(n):
            s += n
    if s == a:
        print(int(s))