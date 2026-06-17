# Strings
print("Strings:")
"""
Strings is a datatype which store multiple
characters one after another which makes a
word. So string can basically be a word or
even a sentence is also a string.
"""
a,b = "hello ","world!"
print("String 'a' is :", a)
print("String 'b' is :", b)

# Basic String Operations
"""
Strings have mainly two basic operations we
can perform on them, these are concatenation
and len or length. Concatenation joins one
string after another and len gives the total
characters in our string.
"""

# Concatenation
print("\nConcatenation:")
"""
Concatenation can be performed using multiple
string separated by plus '+' operator. So we
can write string1+string2 and it will output
as "ValueOfString1ValueOfString2".
"""
c = a+b
print(c)

# Length
print("\nLength")
"""
We can use the len(string) to get the number of
characters in a string, let's try this in string
"a+b".
"""
print(len(c))

# Indexing
print("\nIndexing:")
"""
A string is basically a character array so we
can also use indexing in it as we couldve in a
character array. Let's try printing first and
last character of string "a+b".
"""
print("First character of", c, "is", c[0])
print("Last  character of", c, "is", c[len(c)-1])

# Slicing
print("\nSlicing:")
"""
Slicing allows us to access a substring within a
string by giving a starting index 'a' and an end
index 'b'. Then we will get the substring from a
to b-1 index. Its syntac is str[a:b]. Also if you
try to give a "Negative index", then that index is
counted in reverse from end of the string, but now
this index will start from 1 and not from 0. This
means that -3 index means 3th character from the
end of the string.
"""
print(c[2:len(c)-3]) 
print(c[-10:-3]) # Using Negative Index

# String Functions
print("\nString Functions:")
"""
Following are some of the commonly used string
functions in python:
1. str.endswith("substring")
It returns True if str ends with the passed substring
2. str.capitalize()
It capitalized the first character of str
3. str.replace(old,new)
It replaces all occurrences of old with new
4. str.find("substring")
It finds the starting index of passed substring in str
5. str.count("substring")
It counts the occurrences of passed substring in str
"""
print("c.endswith(\"d!\"):", c.endswith("d!"))
print("c.endswith(\"lo\"):", c.endswith("lo"))
print("c.capitalize() :", c.capitalize())
print("c :", c, "Capitalize is Temporary")
print("c.replace(\"l\",\"L\") :", c.replace("l","L"))
print("c.find(\"world!\") :", c.find("world!"))
print("c.count(\"l\") :", c.count("l"))

# Conditional Statements
"""
Conditional statement are used to evaluate decisions on
runtime to solve various problems depending on scenario.
A good example of conditional statements is if-elif-else
structure. Let's look at its syntax.
"""
marks = float(input("\nEnter Total marks (max:100): "))
if marks>=90 and marks<=100:
    print("A")
elif marks>=80 and marks<90:
    print("B")
elif marks>=70 and marks<80:
    print("C")
elif marks>=50 and marks<70:
    print("D")
elif marks>=0 and marks<50:
    print("F")
else:
    print("Invalid Marks!")