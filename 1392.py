a,b = map(int,input().split())
c = []
d = []
for i in range(a):
    c.append(int(input()))
for j in range(b):
    d.append(int(input()))
for k in range(len(d)):
    e = c[0]
    for l in range(1,len(c)+1):
        if d[k] > e-1:
            e+=c[l]
        else:
            print(l)    
            break