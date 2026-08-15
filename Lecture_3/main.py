# Lists
print("Lists:")
"""
A list is a special array that can store elements
of different datatypes. (intger,float,strings,etc)
List as considered a datatype itself which you can
verify using the type(List_Name).
"""
lis = [4,2,1]
print("type(lis) :", type(lis))
print("lis :", lis)

# Length, Indexing & Slicing:
print("\nLength, Indexing & Slicing:")
"""
You can also use lenght, indexing and slicing in a
list like you can in a string. Count function of
string is also available in list. However, unlike
python strings, python lists are mutable. Which
means you can do "lis[0]=any value" to change
the value at that index of the list, you cannot
changed characters in a string this way.
"""
print("len(lis)     :", len(lis))
print("lis[0]       :", lis[0])
print("lis[1]       :", lis[1])
print("lis[2]       :", lis[2])
print("lis[1:3]     :", lis[1:3])
print("lis.count(2) :", lis.count(2))

# List Methods
print("\nList Methods:")
"""
Methods is just a fancy name for "Functions", so
here are some methods associated with lists that
you can use in python:
1. list.append(element)
It adds element to the back of list
2. list.sort()
It sorts the list elements in ascending order
3. list.sort(reverse=True)
It sorts the list elements in decending order
4. list.reverse()
It reverses the elements in the list
5. list.insert(index,element)
It inserts passed element at the passed index in list
6. list.pop(index)
It removes the element at the passed index of list
7. list.remove(element)
It removes the first occurrence of passed element
"""
lis.append(7)
print("lis after lis.append(7)           :", lis)
lis.sort()
print("lis after lis.sort()              :", lis)
lis.sort(reverse=True)
print("lis after lis.sort(reverse=True ) :", lis)
lis.reverse()
print("lis after lis.reverse()           :", lis)
lis.insert(2,20)
print("lis after lis.insert(2,20)        :", lis)
lis.pop(3)
print("lis after lis.pop(3)              :", lis)
lis.remove(20)
print("lis after lis.remove(20)          :", lis)

# Tuples
print("\nTuples:")
"""
Tuple is like a list that can hold different datatypes,
but it terms of changing elements it is like a string as
you cannot change the value at any index in a tuple. This
means that "tup[0]=any value" is invalid. Also unlike list
whose elements are initialized in [] brackets, elements of
tuple are initialized using (). These brackets are how the
python differentiates a list from a tuple and vice versa.
Just like list, tuple is its own datatype. Also, a tuple
with a single element is considered a datatyoe of that
element unless you put a comma after that element like
"tup=(1,)". If this comma is removed python will see this
tuple as an int.
"""
tup = (3,3,5,1,2)
print("type(tup)    :", type(tup))
print("tup          :", tup)
print("tup[0]       :", tup[0])
print("tup[1]       :", tup[1])
print("tup[2]       :", tup[2])
print("tup[1:4]     :", tup[1:4])

# Tuple Methods
print("\nTuple Methods:")
"""
Following are some methods you can use with tuples in python:
1. tuple.index(element)
It gives the index of first occurrence of that element
2. tuple.count(element)
It gives the number of occurrences of that element
"""
print("tup.index(5) :", tup.index(5))
print("tup.count(3) :", tup.count(3))