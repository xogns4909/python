num = int(input())
size = []
left = 0
l_flag =0
right = 0
r_flag=0
for i in range(num):
    size.append(int(input()))
for j in range(num):
    if(size[j]>l_flag):
        l_flag = size[j]
        left += 1
for k in range(num-1,-1,-1):
    if(size[k]>r_flag):
        r_flag = size[k]
        right += 1
print(left,right)           