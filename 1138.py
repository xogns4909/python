a = int(input())
b = list(map(int,input().split()))
result= [0]*a
for i in range(a):
    count =0
    for j in range(a):
        if count == b[i] and result[j] ==0:
            result[j] = i+1
            break
        elif(result[j] == 0):
            count +=1    
print(*result)            