#1.
lst=list(map(int,input("Enter a value with spaces").split()))
print(f"Actual list is {lst}")
even=[]
odd=[]
for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"Even list is {even}")
print(f"Odd list is {odd}")
#output
# Enter a value with spaces1 2 3 4 5 6
# Actual list is [1, 2, 3, 4, 5, 6]
# Even list is [2, 4, 6]
# Odd list is [1, 3, 5]
#2.
s=input("Enter a string:")
print("Given string is:",s)
reverse=""
for i in range(len(s)-1,-1,-1):
    reverse+=s[i]
print("Reversed string is:",reverse)
#output
# Enter a string: hello
# Given string is: hello
# Reversed string is: olleh
#3.
x=int(input("Enter x value:"))
y=int(input("Enter y value:"))
z=int(input("Enter z value:"))
class A:
	def show1(self,x):
		self.a=x
class B(A):
	def show2(self,y):
		self.b=y
class C(B):
	def show3(self,z):
		self.c=z
	def display(self):
		print("x value is",self.a)
		print("y value is",self.b)
		print("z value is",self.c)
ml= C()
ml.show1(x)
ml.show2(y)
ml.show3(z)
ml.display()
#output
# Enter x value:10
# Enter y value:20
# Enter z value:30
# x value is 10
# y value is 20
# z value is 30
