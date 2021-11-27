arr = [list(map(int, input().split())) for _ in range(9)]
x = 0
y = 0
Max = 0
for i in range(9):
    if max(arr[i]) > Max:
        Max = max(arr[i])
        x =i + 1
        y = arr[i].index(Max)+1
print(Max)
print(x , y)        