a =[]
b =[]
for i in range(7):
    a.append(int(input()))
for j in range(len(a)):
    if a[j] % 2 == 1:
        b.append(a[j])
if len(b) != 0:       
    print(sum(b))
    print(min(b))
else:
    print(-1)