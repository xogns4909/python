a = int(input())
c = []
for i in range(3):
    b = 0
    for j in range(a):
        d = int(input())
        b += d
    c.append(b)    
for i in range(3):
    if c[i] > 0:
        print('+')
    elif c[i] < 0:
        print('-')
    else:
        print(0)            