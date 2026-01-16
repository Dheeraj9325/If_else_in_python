a = int(input("Enter a number:"))
b = 0
while a > 0:
    D = a % 10
    b = b + D
    a = a // 10 
print(b)