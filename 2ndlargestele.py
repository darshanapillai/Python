list=[]
s=eval(input("Enter the size of list"))
print('Enter the elements')
for i in range(0,s):
    number=int(input())
    list.append(number)
print("The elements in the list are:",list)
list.sort()
second=list[-2]
print("the second largest element is:",second)