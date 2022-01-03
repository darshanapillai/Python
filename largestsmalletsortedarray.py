lst=[]
n=eval(input("enter the size of array"))
print("emter the elements:")

for i in range(0,n):
    number=int(input())
    lst.append(number)
print("The elemets in array are:",lst)
lst.sort()
print("The sorted array is",lst)
print("The max element is:",max(lst))
print("The min element is:",min(lst))