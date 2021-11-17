a = int(input())
b = "0b"
b += str(a)
c =int(b,2)
print(bin(c*17)[2:])