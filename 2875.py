a,b,c = map(int,input().split())
while(c!=0):
    if 2*b > a:
        b -=1
        c-=1
    elif 2*b<=a:
        a -= 1
        c-= 1 
print(min(a//2,b))           