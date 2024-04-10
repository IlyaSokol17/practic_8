s = ''
for i in range (1, 10):
    s += str(i)
    sum = int(s) * 8 + i
    print(f'{s} * 8 + {i} = {sum}')

s = ''
for i in range (1, 10):
    s += str(i)
    sum = int(s) * 9 + (i + 1)
    print(f'{s} *  + {i + 1} = {sum}')

s = ''
for i in range (0, 9):
    s += '1'
    sum = int(s) * int(s)
    print(f'{s} * {s} = {sum}')