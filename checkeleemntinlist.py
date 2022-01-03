list=[]
s=eval(input("enter the size of list"))
print("Enter the elements in list:")
for i in range(0,s):
    number=int(input())
    list.append(number)
print("The elements in list are:",list)

check=eval(input("Enter the element to be checked in list:"))
if check in list:
    print("Yes the element",check,"exists")
else:
    print("Doesn't exist!!")
