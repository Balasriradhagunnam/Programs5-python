#1(1).
a=int(input("enter a value: "))
b=int(input("enter b value: "))
print("Addition:", a + b)   
print("Subtraction:", a - b)    
print("Multiplication:", a * b)  
print("Division:", a / b)       
print("Modulus:", a % b)        
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)
# Output
# enter a value: 4
# enter b value: 2
# Addition: 6
# Subtraction: 2
# Multiplication: 8
# Division: 2.0
# Modulus: 0
# Exponentiation: 16
# Floor Division: 2
#1(2).
x=int(input("enter x value: "))
y=int(input("enter y value: "))
print("x > y:", x > y)
print("x < y:", x < y)   
print("x == y:", x == y)
print("x != y:", x != y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
# Output
# enter x value: 4
# enter y value: 5
# x > y: False
# x < y: True
# x == y: False
# x != y: True
# x >= y: False
# x <= y: True
#1(3)
x=int(input("enter x value: "))
y=int(input("enter y value: "))
z=x
print(x is y)
print(x is not y)
print(x is z)
# Output
# enter x value: 20
# 2enter y value: 30
# False
# True
# True
#2.
side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
# Output
# Enter first side: 3
# Enter second side: 4
# Enter third side: 6
# The triangle is valid.
#3.
s=input("Enter a String")
temp=s
rev=""
for i in range(len(s)-1, -1, -1):
    rev+=s[i]
if(temp==rev):
    print("It is a palindrome string")
else:
    print("It is not a palindrome string") 
# Output
# Enter a String: madam
# It is a palindrome string
