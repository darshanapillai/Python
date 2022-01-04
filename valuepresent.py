dictionary={1:1,2:2}
print(dictionary)
n=eval(input("enter the value to search"))
if n in dictionary.values():
    print("Yes present..!!")
else:
    print("not present!")