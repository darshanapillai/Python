s=input("Enter a string:")
element=input("Enter the word to be counted:")
words=s.split()
count=0
for i in words:
    if i == element:
        count+=1
print("The no of occurance is:", count)

