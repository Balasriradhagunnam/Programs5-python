#1.
a=input("enter your character: ")
list1=['a','e','i','o','u']
if a in list1:
    print("vowel")
else:
    print('consonant')
#output
# enter your character: a
# vowel
#2.
lst=list(input("Enter a value with spaces").split())
print(f"Actual list is {lst}")
min_pos=lst.index(min(lst))
max_pos=lst.index(max(lst))
print(f"Minimum valued Position is {min_pos}")
print(f"Maximum valued Position is {max_pos}")
#output
# Enter a value with spaces4 2 5 1
# Actual list is ['4', '2', '5', '1']
# Minimum valued Position is 3
# Maximum valued Position is 2
#3.
def factorial(n):
	if n==0:
		return 1
	else:
		return n* factorial(n-1)
num=int(input("enter the value"))
print(f"Factorial of {num} is {factorial(num)}")
#output
#enter the value 5
#Factorial of 5 is 120
