arr=[10,20,30,40,50]
s=0;
for i in range(0,len(arr)):
    s=s+arr[i]

print("sum of array is",s)

#Method 2 taking user input

arr=[]
num=eval(input("Enter the size of array"))
print("Enter the elements:")
for i in range(num):
    number=int(input())
    arr.append((number))
print("The elemets in array are",arr)
s=0;
for i in range(0,len(arr)):
    s=s+arr[i]

print("The sum of array is:",s)