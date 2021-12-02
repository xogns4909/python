string = input()
cnt = 0
for i in string:
    if i == ' ':
        cnt +=1
if string[-1] == ' ':
    cnt -= 1
if string[0] == ' ':
    cnt -= 1
print(cnt+1)