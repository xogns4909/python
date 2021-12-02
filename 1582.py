pe, count, rul = map(int, input().split())
li = [0]*pe
cnt = i = 0
while li[i] < count-1:
    li[i] += 1
    cnt += 1
    i = (i+rul)%pe if li[i]%2 == 1 else (i-rul)%pe
print(cnt)