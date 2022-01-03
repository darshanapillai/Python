list=[]
s=eval(input("Enter the size of list:"))
print("Enter the elements :")
for i in range(0,s):
    number=int(input())
    list.append(number)

print("The elemts in the list are as follows:",list)
list2=[]
for j in list:
    if j%2 == 0:
        list2.append(j)
print("Even no in list are:",list2)
