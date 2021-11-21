c = []
d =0
for i in range(4):
    a,b = map(int,input().split())
    d += b - a
    c.append(d)
print(max(c))    