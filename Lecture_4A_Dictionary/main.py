'''
Lecture: 4

Topic: Dictionary
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

# Key:Value insertion in Dictionary
name_key = input("Enter key for name: ")
dummy[name_key] = input("Enter value for name: ")

# Key:Value insertion in Dictionary
age_key = input("Enter key for age: ")
dummy[age_key] = input("Enter value for age: ")

# Print number of keys in Dictionary
print(len(dummy))

# Print entire Dictionary
print(dummy)

# Print type of Dictionary
print(type(dummy))

# Print value of a specifice key
name = dummy[name_key]
print(name)
age = dummy[age_key]
print(age) 

# Basic Dicionary Methods Section
print("Basic Dictionary Methods:")

'''
Basic Dictionary Methods:
Following are some basic methods used with Dictionary in python.

1. dict_name.keys()
It returns all keys in that Dictioary

2. dict_name.values()
It returns all values in that Dictioary

3. dict_name.items()
It returns all key:value pairs as tuples. You can do indexing in
the returned tuples if you type cast the retuned tuples to list/tuple.

4. dict_name.get("key")
It returns the value of passed key. Similar to dict_name["key"]
but wont crash if key isn't found so safer than dict_name["key"]

5. dict_name.update(new_dict)
It inserts the passed items in the Dictionary
'''

# Print all keys
dummy_keys = dummy.keys()
print(dummy_keys)

# Print all values
dummy_values = dummy.values()
print(dummy_values)

# Print key:value pairs as a List
pairs = list(dummy.items())
print(pairs)

# Print specific tuple from the returned tuples using index.
index_val = pairs[0]
print(index_val)

# Print value using dict_name.get("key")
dummy_name = dummy.get(name_key)
print(dummy_name)
dummy_age = dummy.get(age_key)
print(dummy_age)

# Add More key:value pair using dict_name.update({pairs})
new_pairs = {}
gender_key = input("Enter key for gender: ")
new_pairs[gender_key] = input("Enter value for gender: ")
isAdult_key = input("Enter key for isAdult: ")
new_pairs[isAdult_key] = input("Enter value for isAdult: ")
dummy.update(new_pairs)
print(dummy)
# old key:value pairs can be updated as well by using existing keys

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

# Print number of keys in Parent Dictionary
print(len(parent_dict))

# Print number of keys in Child Dictioary
print(len(parent_dict["child1_dict"]))
print(len(parent_dict["child2_dict"]))

# Print Parent Dictionary:
print(parent_dict)

# Print values of specific keys of Parent Dictionary
child1 = parent_dict["child1_dict"]
print(child1)
child2 = parent_dict["child2_dict"]
print(child2)

# Print values of specific keys of Child Dictionary
child1_name = parent_dict["child1_dict"]["ch1_name"]
print(child1_name)
child1_age = parent_dict["child1_dict"]["ch1_age"]
print(child1_age)
child2_name = parent_dict["child2_dict"]["ch2_name"]
print(child2_name)
child2_age = parent_dict["child2_dict"]["ch2_age"]
print(child2_age)

# Print all keys of Parent Dictionary
parent_keys = parent_dict.keys()
print(parent_keys)

# Print all values of Parent Dictionary
parent_values = parent_dict.values()
print(parent_values)

# Print all key:value pairs of Parent Dictionary
parent_pairs = parent_dict.items()
print(parent_pairs)

# Print all keys of Child Dictionary
child1_keys = parent_dict["child1_dict"].keys()
print(child1_keys)
child2_keys = parent_dict["child2_dict"].keys()
print(child2_keys)

# Print all values of Child Dicionary
child1_values = parent_dict["child1_dict"].values()
print(child1_values)
child2_values = parent_dict["child2_dict"].values()
print(child2_values)

# Print all key:value pairs of Child Dictioary
child1_pairs = parent_dict["child1_dict"].items()
print(child1_pairs)
child2_pairs = parent_dict["child2_dict"].items()
print(child2_pairs)