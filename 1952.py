import sys
N, C = map(int, sys.stdin.readline().split())
check = [False]*(C+1)
ans = 0

for _ in range(N):
    n = int(sys.stdin.readline())
    for i in range(n, C+1, n):
        if check[i]==False:
            check[i] = True
            ans += 1
print(ans)