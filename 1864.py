a = " "
d = []
while(a !='#'):
    a = input()
    c = 1
    b = []
    result = []
    for i in range(len(a)):
        if a[i] =='-':
            b.append(0)
        elif a[i] == '\\':
            b.append(1)    
        elif a[i] =='(':
            b.append(2)
        elif a[i] =='@':
            b.append(3)
        elif a[i] =='?':
            b.append(4)
        elif a[i] =='>':
            b.append(5)
        elif a[i] == '&':
            b.append(6)
        elif a[i] =='%':
            b.append(7)
        elif a[i] =='/':
            b.append(-1)
    for i in range(len(b)):
        result.append((b[i]*(8**(len(b)-c))))
        c+=1
    d.append((sum(result)))
for j in range(len(d)-1):
    print(d[j])