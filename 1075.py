result =0
a =[]
for i in range(8):
    a.append(list(str(input())))
for j in range(8):
     for k in range(8):
         if(j+k)%2==0:
             if(a[j][k]=='F'):
                 result+=1
print(result)                

