list=[]
s=eval(input("Enter the size of list"))
print("Enter the elements:")
for i in range(0,s):
    number=int(input())
    list.append(number)
print("elements in list are:",list)

x=eval(input("Enter the position to be swapped:"))
y=eval(input("Enter the position to be swapped with:"))
temp=list[x]
list[x]=list[y]
list[y]=temp
print("The list after swapping is:",list)