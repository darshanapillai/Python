list=[]
s=eval(input("Enter the size of list"))
print("Enter the elements")
for i in range(0,s):
    number=int(input())
    list.append(number)
print("The elements in list are:",list)
list2=[]
for j in list:
    if j<0:
        list2.append(j)
print("Negavtive no in list are:",list2)