a = 10203040
b = 0
c = 0
while a > 0:
    D = a % 10
    b = D
    a = a // 10
    if b != 0:
        c = c*10+b
        while a > 0 and a % 10 ==0:
            a = a//10
print(c)