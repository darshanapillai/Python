list=[]
s=eval(input("Enter size of list"))
print("Enter the elemets:")
for i in range(0,s):
    number=int(input())
    list.append(number)
print("The elements in list are:",list)

list2=[]
for j in list:
    if j not in list2:
        list2.append(j)
print("The  removl of duplicates elements are:",list2)


for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if(list[i] == list[j]):
            print("Th duplicate elements are:",list[j])




