import sys
student,hate=sys.stdin.readline().split()
student=int(student)
cnt=0
n=0
while cnt!=student:
    n+=1
    if hate in str(n):
        continue
    cnt+=1
print(n)