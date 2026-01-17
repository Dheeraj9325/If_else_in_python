a = int(input("Enter number: "))
b = 0
while a > 0:
    D = a % 10
    a = a // 10
    if D > b:
        b = D
print(b)