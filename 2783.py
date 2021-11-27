a,b = map(int,input().split())
c = a*1000/b
d = int(input())
for i in range(d):
    x,y=map(int,input().split())
    e = x*1000/y
    if c > e:
        c = e
print(round(c,2))        
