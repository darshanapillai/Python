s=input("Enter a string:")
element=input("Enter the element to be counted:")
count=0
for i in s:
    if i == element:
        count = count+1
print("No of occourance is:", count)


