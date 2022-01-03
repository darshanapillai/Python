lst=[]
n=eval(input("Enter the size of the array"))
print("Enter the elements:")
for i in range(0,n):
    number=int(input())
    lst.append(number)
print("The list is ",lst)
rev=lst[::-1]
print("The reverse list is :",rev)
