array=[[]]
row ,col = map(int,input().split())
cnt = 0
for i in range(row):
    for j in range(col):
        array[i][j] = input()
for k in range(row):
    if array[k] in 'X':
       continue
    else:
        cnt+=1
print(cnt)          