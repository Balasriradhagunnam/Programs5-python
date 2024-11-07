#1.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)
# Output
# Enter the first number: 4
# Enter the second number: 5
# Enter the third number: 0
# The largest number is: 5
# 2.
def find_second_largest(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort()            #brings to ascending order 
    return unique_lst[-2]        #As ascending,last to 2nd element will be largest

numbers = [3, 5, 9, 2, 8]
print(find_second_largest(numbers))
#output
# 8
#3.
distance = float(input("Enter the distance in kilometers: "))
time_minutes = float(input("Enter the time in minutes: "))
time_hours = time_minutes / 60
speed = distance / time_hours
print("The speed is:", speed, "km/h")
# output
# Enter the distance in kilometers: 120
# Enter the time in minutes: 60
# The speed is: 120.0 km/h
