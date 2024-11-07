#1.
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)
# Output
# Enter the length of the rectangle: 10
# Enter the width of the rectangle: 6
# The area of the rectangle is: 60
# The perimeter of the rectangle is: 32
#2.
dict1 = {1:'A',2:'B',3:'C'}
print("Original dictionary:", dict1)
new_key = input("Enter the key you want to add: ")
new_value = input("Enter the value for the new key: ")
dict1[new_key] = new_value
print("Updated dictionary:",dict1)
# Output
# Original dictionary: {1: 'A', 2: 'B', 3: 'C'}
# Enter the key you want to add: 4
# Enter the value for the new key: D
# Updated dictionary: {1: 'A', 2: 'B', 3: 'C', '4': 'D'}
#3.
n1=int(input("enter x value:"))
n2=int(input("enter y value:"))
class constructor:
	def para(self,n1,n2):
		self.x=n1
		self.y=n2
	def display(self):
		print("x value is",self.x)
		print("y value is",self.y)
p=constructor()
p.para(n1,n2)
p.display()
#output
# enter x value:10
# enter y value:20
# x value is 10
# y value is 20
