arr=[]
n=eval(input("Enter the size of array:"))
print("enter the elements are:")
for i in range(0,n):
    number=int(input())
    arr.append(number)
print("The array is :",arr)

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp


print("elemngts after sorting are:",arr)