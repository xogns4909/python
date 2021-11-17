time = []
for i in range(3):
    a = list(map(int,input().split()))
    time.append((a[3] *3600 + a[4] * 60 + a[5]) - (a[0] * 3600 + a[1] *60 + a[2]))
for j in range(3):
    print(time[j]//3600,time[j] % 3600 //60,time[j]%3600%60)