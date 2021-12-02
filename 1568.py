bird = int(input())
cnt =0
i =1
while(bird != 0):
    if(bird - i >= 0):
        bird -= i
        i += 1
        cnt +=1
    else:
        i = 1
print(cnt)        
