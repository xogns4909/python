d = []
a = 1
while a != '0':
    a = str(input())
    b = a.count('1')
    c = a.count('0')
    d.append(len(a)*3+b*-1+c*1+len(a)+1)
for i in range(len(d)-1):
    print(d[i])
    
