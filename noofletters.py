s=input("Enter a string:")
word=len(s)-s.count(" ")
print("The no of letters are",word)

#Method 2 using loop

s=input("Enter a string:")

count=0
for i in s:
    count+=1
    count=count-i.count(" ")
print(count)