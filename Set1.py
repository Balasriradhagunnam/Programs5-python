#1.
f=int(input("enter fahrenheit temperature"))
c=((f-32) *5)//9;
print(f"celcius temperature is {c}")
#output
# enter fahrenheit temperature98
# celcius temperature is 36
#2.
a=int(input("enter a"))
b=int(input("enter b"))
print(f"a is {a} and b is {b}")
a,b =b,a
print(f"a is {a} and b is {b}")
#output
# enter a4
# enter b5
# a is 4 and b is 5
# a is 5 and b is 4
#3.
key=int(input("Enter your key value"))
dic={1:'a',2:'b',3:'c'}
print("The Dictionary is",dic)
if key in dic:
	print("Key is Present")
else:
	print("Key is not present")
#output
#Enter your key value 3
#The Dictionary is {1:'a',2:'b',3:'c'}
#Key is Present
