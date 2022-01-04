dict={1:"Hey","Name":"darshu","colors":["red","blue","green"]}
print(dict)
print(dict["colors"])

# get() method returns a particular value
print(dict.get("Name"))

# keys() method returns all the keys
x=dict.keys()
print(x)

# values() method returns all the values
x=dict.values()
print(x)

# items() method will return each item in a dictionary, as tuples in a list.
x=dict.items()
print(x)

# update() method will update the dictionary with the items from the given argument.
dict.update({"Name":"Darshana Pillai"})
print(dict)

#The pop() method removes the item with the specified key name:
dict.pop(1)
print(dict)

#The popitem() method removes the last inserted item
dict.popitem()
print(dict)

dict["Age"]="22"
dict["City"]="Bhopal"
print(dict)

#Copy a Dictionary
# using copy()
newdict=dict.copy()
print(newdict)

#using dict()
new=dict(dict)
print(new)