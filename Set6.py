#1.
lst=list(map(int,input("Enter a value with spaces:").split()))
print(f"Actual list is {lst}")
lst[0],lst[-1]=lst[-1],lst[0]
print(f"After Interchanging {lst}")
#output
# Enter a value with spaces:1 2 3 4 5 
# Actual list is [1, 2, 3, 4, 5]
# After Interchanging [5, 2, 3, 4, 1]
#2.
input_string = input("enter your sentence")
print(input_string)
words = input_string.split()
print(words)
for word in words:
    if len(word) % 2 == 0:
        print(word)
#output
# enter your sentenceI am raghu
# I am raghu
# ['I', 'am', 'raghu']
# am
# 3.
f=open('sample.bin','wb')
f.write(b"hello python")
f.close()
f=open('sample.bin','rb')
print(f.read())
f.close()
# Output
# hello python
