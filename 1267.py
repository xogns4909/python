a = int(input())
b = list(map(int,input().split()))
c = 0
d = 0
for i in range(len(b)):
    c += (b[i] // 30 + 1) * 10
    d += (b[i] // 60 + 1) *15
if c > d:
    print('M',d)
elif d > c:
    print('Y',c)
else:
    print('Y','M',d)            