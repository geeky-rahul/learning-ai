# Slicing
num_list = "0123456789"
print(num_list[:]) 
print(num_list[3:])
print(num_list[:8])
print(num_list[3:10:2])
print(num_list[0:-1])
print(num_list[3:4])
print(num_list[3:8:-1])
print(num_list[8:3:-1])

#Methods in strings
name = " Rahul Kumar GUpta "
print(name.lower())
print(name.upper())
print(name.strip())
print(name.replace("Kumar",""))
print(len(name))
print("Kumar" in name)
print("kumar" in name)

flowers = "Rose, lily, lotus"
print(flowers.split())
print(flowers.split(", "))
print(name.find("Kumar"))
print(name.find("K"))
print(name.find("N")) # output -1 becasue char "N" not exist in name
print(name.count("a"))

# list to string
my_name = ['Rahul', 'Kumar', 'Gupta']
print("".join(my_name))
print(" ".join(my_name))
print("-".join(my_name))

# print "" \n
chai = "He said, \"Masala chai is awesome\""
print(chai)
print("Rahul\nkumar")
print(r"Rahul\nkumar") # Raw string