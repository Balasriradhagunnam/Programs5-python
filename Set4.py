#1.
year=int(input("enter year"))
if(year%4==0 and year%100!=0) or (year%400==0):
    print("LEAP YEAR");
else:
    print("Not leap year");
# Output
# enter year1600
# LEAP YEAR
#2.
list1 = input("Enter the first list of strings separated by space: ").split()
list2 = input("Enter the second list of strings separated by space: ").split()
concatenated_list = []
print(list1)
print(list2)
for i in range(len(list1)):
    concatenated_list.append(list1[i] + list2[i])
print("Concatenated List:", concatenated_list)
#output
# Enter the first list of strings separated by space: M na i Abhi
# Enter the second list of strings separated by space: y me s Ram
# ['M', 'na', 'i', 'Abhi']
# ['y', 'me', 's', 'Ram']
# Concatenated List: ['My', 'name', 'is', 'AbhiRam']
#3.
def gcd_recursion(a,b):
	if b==0:
		return a
	else:
		return gcd_recursion(b,a%b)
num1=int(input("Enter a value"))
num2=int(input("Enter b value"))
print(f"The GCD value of {num1} and {num2} is {gcd_recursion(num1,num2)}")
#output
#Enter a value 48
#Enter b value 18
#The GCD value of 48 and 18 is 6
