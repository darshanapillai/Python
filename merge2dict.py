dict1={1:"a",2:"b"}
dict2={3:"c",4:"d"}

#using **
res={**dict1,**dict2}
print(res)

#using update

dict1.update(dict2)
print(dict1)

