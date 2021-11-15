a,b = map(int,input().split())
c = int(input())
if c+b >= 60:
    a = a + (c+b)//60
    c = (c+b) % 60
    if a >=24:
        a = a-24
    print(a,c)

else:    
    print(a,b+c)     
