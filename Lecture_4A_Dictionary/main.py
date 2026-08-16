'''
Lecture: 4

Topic: Dictionary & Set
'''

# Dictionary Section
print("Topic: Dictionary:")

'''
Dictionary:
Python dictionary works by saving key value pairs.
In nature, you can say it's similar to c++ hashmaps.
You save data using key:value pairs, then you just
search for the key and you receive the value if that
key exists in your dictionary. Dictionary is mutable
which means that the value associated with a certain
key can be changed unlike the values of a tuple which
are immutable.
'''

# Dictionary Declaration
dummy = {}

# Python Inputs
name_key = input("Enter key for name: ")
name_value = input("Enter value for name: ")

# Key:Value insertion in Dictionary
dummy[name_key] = name_value

# Python Inputs
age_key = input("Enter key for age: ")
age_value = input("Enter value for age: ")

# Key:Value insertion in Dictionary
dummy[age_key] = age_value

# Print entire Dictionary
print(dummy)

# Print type of Dictionary
print(type(dummy))

# Print value of a specifice key
print(dummy[name_key])
print(dummy[age_key]) 

# Print all keys as a List
print(list(dummy.keys()))

# Print all values as a List
print(list(dummy.values()))

# Nested Dictoinary Section
print("Topic: Nested Dictioary")

'''
Nested Dictionary:
A Dictionary can also be kept as a key:value pair in a Dictionary.
Child Dictionary's name becomes the key and its key:value pairs
become the values associated with that key.
'''

# Dictionary Declaration
parent_dict = {}

# Kay:Value insertion of a Child Dictionary
parent_dict["child1_dict"] = { "ch1_name":"kaido", "ch1_age":80 }
parent_dict["child2_dict"] = { "ch2_name":"luffy", "ch2_age":21 }

# Print Parent Dictionary:
print(parent_dict)

# Print values of specific keys of Parent Dictionary
print(parent_dict["child1_dict"])
print(parent_dict["child2_dict"])

# Print values of specific keys of Child Dictionary
print(parent_dict["child1_dict"]["ch1_name"])
print(parent_dict["child1_dict"]["ch1_age"])
print(parent_dict["child2_dict"]["ch2_name"])
print(parent_dict["child2_dict"]["ch2_age"])

# Print all keys of Parent Dictionary as a List
print(list(parent_dict.keys()))

# Print all values of Parent Dictionary as a List
print(list(parent_dict.values()))

# Print all keys of Child Dictionary as a List
print(list(parent_dict["child1_dict"].keys()))
print(list(parent_dict["child2_dict"].keys()))

# Print all values of Child Dicionary as a List
print(list(parent_dict["child1_dict"].values()))
print(list(parent_dict["child2_dict"].values()))