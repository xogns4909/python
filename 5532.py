a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if b % d == 0:
   b_ = b // d
else:
    b_ = b // d + 1
if c % e == 0:
   c_ = c // e
else:
    c_ = c // e + 1
print(a -max(b_,c_))                 