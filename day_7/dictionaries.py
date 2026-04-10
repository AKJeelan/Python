customer = {
    "name" : "Abdul Jeelan",
    "age" : 28,
    "is_verified" : True

}

print(customer)
print(customer["name"])
# print(customer["birth_day"]) #Error no key present in the dictionary

customer["birth_day"] = "01 Jan 1998"

print(customer)
print(customer.get("birth_day"))
print(customer.get("colllege","RYMEC")) # if key not present will pass the default value