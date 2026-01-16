a = int(input("Enter a number:"))
z=a
b = 0
while a > 0:
    D = a % 10
    b = b*10 + D
    a = a // 10 
if z == b:
    print("Palindrome")
else:
    print("Not palindrome")