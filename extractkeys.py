dictionary={"name":"darshana","age":"22","city":"banglore"}
keys=["name","age"]

res=dict()
for k in keys:
    res.update({k:dictionary[k]})
print(res)


#2nd method
keys=["city"]
newdict={k:dictionary[k] for k in keys}
print(newdict)
