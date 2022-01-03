s=(input("Enter a sentence"))
v=0
c=0
for i in s:
    if(i=='A' or i=='E'or i=='I'or i=='O' or i=='U' or i=='a'or i=='e'or i=='i'or i=='o' or i=='u'):
        v=v+1

    else:
        c=c+1
print("No of vowels are:",v)
print("No of consonents are",c)