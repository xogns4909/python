level = int(input())
a = 0
for i in range(level+2):
    a += i
for j in range(2,level+2):
    a += j
for k in range(0,level):
    a += k
print(a%45678)