user_data = {"Name": "Rahul",
             "Age": 20,
             "Address": "Delhi"}
print(user_data)
print(user_data["Name"])
print(user_data.get("Name"))
# print(user_data["namme"]) # error
print(user_data.get("namme")) # output: None
user_data["Age"] = 21
print(user_data["Age"])

# Loops in Dict
for data in user_data:
    print(data) # it gives only keys  
    
for data in user_data:
    print(data, user_data[data])
    
for key, value in user_data.items():
    print(key, value)
    
squared_num = {x:x**2 for x in range(10)}
print(squared_num)
    
# Condition in dict
if "Name" in user_data:
    print("Yes")
    
# Methods in dict
print(len(user_data))
user_data["College"] = "Ramanujan College"
print(user_data["College"])
print(user_data.pop("College"))
# print(user_data["College"]) # Output: Error
print(user_data.popitem())
del user_data["Age"]
print(user_data)
squared_num.clear()
print(squared_num) # Output empty dict

# Nested Dict
tea_shop = {
    "chai": {
        "masala": "Spicy",
        "Ginger": "Zesty"   
    },
    "Tea": {
        "Green": "Mild",
        "Black": "Strong"
    }
}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])

# Creating dict using list
keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
new_dict = dict.fromkeys(keys, keys)
print(new_dict)