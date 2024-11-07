#1.
marks = int(input("Enter marks: "))
if marks >= 90:
    grade = "Grade A"
elif marks >= 80:
    grade = "Grade B"
elif marks >= 70:
    grade = "Grade C"
elif marks >= 60:
    grade = "Grade D"
elif marks >= 50:
    grade = "Grade E"
else:
    grade = "Failed"
print("Your grade is:", grade)
# Output
# Enter marks: 90
# Your grade is: Grade A

#2(1).
x=int(input("enter x value"))
print(x<5 and x<10) 
print(x<5 or x<4)  
print(not(x>10))    
# Output
# enter x value6
# False
# False
# True

#2(2).
x=int(input("enter x value"))
y=int(input("enter y value"))
print(x&y)
print(x|y)
print(x^y)
print(~x)
print(x<<1)
print(x>>1)
# Output
# enter x value5
# enter y value3
# 1
# 7
# 6
# -6
# 10
# 2

#3.
import csv
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["John", 28, "newyork"])
    writer.writerow(["Sara", 22, "losangles"])
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# Output
# ["Name", "Age", "City"]
# ["John", 28, "newyork"]
# ["Sara", 22, "losangles"]
