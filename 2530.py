h,m,s = map(int,input().split(" "))
sec = int(input())


s1 = (s+sec)%60 
m1 = (s+sec)//60

m2 = (m+m1)%60 
h1 = (m+m1)//60

h2 = (h+h1)%24 

print(h2,m2,s1) 
# a,b,c = map(int,input().split())
# d = int(input())
# c = c + d
# if c >= 60:
#     b += c // 60
#     c = c % 60
#     if b >= 60:
#         a += b // 60
#         b = b % 60
#         if a >= 24:
#             a= a-24 
#     print(a ,b, c)               
# else:
#     print(a,b,c)        