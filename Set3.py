#1.
lst=list(map(int,input("Enter the values seperated with spaces: ").split()))
print(lst)
sum=0
for i in lst:
    sum+=i
print("Sum is",sum)
avg=sum//len(lst)
print("Average is",avg)
#output
# Enter the values seperated with spaces: 1 2 3 4 5
# [1, 2, 3, 4, 5]
# Sum is 15
# Average is 3
#2.
f=open('sample.txt','w')
f.write("hello python")
f.close()
f=open('sample.txt','r')
print(f.read())
f.close()
# Output
# hello python
#3.
def fibonocci(n):
	if n<=1:
		return n
	else:
		return (fibonocci(n-1) +fibonocci(n-2))
num=int(input("enter a value"))
if num<=0:
	print("Please enter a positive number")
else:
	print("Fibonocci series are")
	for i in range(num):
		print(fibonocci(i),end=' ')
#Output
#Fibonocci series are
# 0 1 1 2 3 
