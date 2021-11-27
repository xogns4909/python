a =[]
e = int(input())
for i in range(e):
    a.append(int(input()))
    b,c,d,f=0,0,0,0
    while a[i] != 0:
        if a[i] >= 25:
             a[i] -=25
             b += 1
        elif a[i] >= 10:
            a[i] -=10
            c+=1 
        elif a[i] >= 5:
            a[i] -=5
            d+=1
        elif a[i] >= 1:
            a[i] -= 1
            f += 1
    print(b, c, d,f)                 
