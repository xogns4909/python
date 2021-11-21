a = int(input())
c = []
for i in range(a):
    b = []
    b = list(map(int,input().split()))
    for j in range(2):
        if b.count(b[j]) == 3:
            c.append(10000+b[j]*1000)
            break
        elif b.count(b[j]) == 2:
            c.append(1000+b[j]*100)
            break
    c.append(max(b)*100)
print(max(c))        
