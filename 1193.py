a = int(input())
b = 0
i = 0
while a > b:
    i +=1
    b += i
if i% 2 == 0:
    c = i-(b-a)
    d = 1+(b-a)
else:
    c =1+(b-a)
    d =i-(b-a) 
print (str(c)+'/'+str(d))    