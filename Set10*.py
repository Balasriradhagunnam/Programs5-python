s=input("Enter a String")
temp=s
rev=""
for i in range(len(s)-1, -1, -1):
    rev+=s[i]
if(temp==rev):
    print("It is a palindrome string")
else:
    print("It is not a palindrome string") 
