a = 1234
b = 0
while a > 0:
    D = a % 10
    b = b*10 + D
    a = a // 10
print(b)