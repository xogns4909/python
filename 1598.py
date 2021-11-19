a,b = map(int,input().split())
c = []
e = []
if a % 4 == 0:
    c.append(4)
    a = a // 4 
else:
    c.append(a%4)
    a = a //4 +1
if b % 4 == 0:
    c.append(4)
    b = b //4
else:
    c.append(b%4)
    b = b// 4 + 1
e.append(a)
e.append(b)
print(max(c)-min(c)+max(e)-min(e) )                        
