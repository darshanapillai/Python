list=[]
s=eval(input("Enter the size of list"))
print("Enter the elements:")
for i in range(0,s):
    number=int(input())
    list.append(number)
print("elements in list are:",list)
temp=list[0]
list[0]=list[-1]
list[-1]=temp
print("elements in list after interchange  are:",list)

