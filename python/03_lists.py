tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities)
print(tea_varities[-1])
print(tea_varities[2:])
print(tea_varities[1:1]) # Output Empty list because [1:1] means include 1 and exclude 1 end result is empty
print(tea_varities[3])
tea_varities[3] = "Herbal"
print(tea_varities)

tea_varities[1] = "Lemon"
print(tea_varities)
# tea_varities[2:3] = "Ginger" #treated as array
# print(tea_varities) # output ['Black', 'Lemon', 'G', 'i', 'n', 'g', 'e', 'r', 'Herbal']
tea_varities[2:3] = ["Ginger"]
print(tea_varities)
tea_varities[1:1] = ["test", "test"] # It means insert this at position 1
print(tea_varities)
tea_varities[1:1] = []
print(tea_varities)
tea_varities[1:3] = []
print(tea_varities)


# Condition and loops in list
for tea in tea_varities:
    print(tea, end="-")
    
if "Oolong" in tea_varities:
    print("\nI have Lemon tea")
print()   


# Methods in lists
tea_varities.append("Oolong")
print(tea_varities)
print(tea_varities.pop()) # Delete last value of the list, output is Oolong i.e last value 
print(tea_varities) # Output: ['Black', 'Lemon', 'Ginger', 'Herbal']
print(tea_varities.remove("Ginger")) # Output None
print(tea_varities)
print(tea_varities.insert(1, "Green")) # Output



