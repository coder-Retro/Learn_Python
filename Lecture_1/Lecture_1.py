# Python Basics:

# Displaying Output:
print("Displaying Kaido");

# Variables:
name = "Kaido"    # String
age = 21          # Integer
height = 5.5      # Float
hobby = "coding"  # String
alive = True      # Boolean
empty = None          # None
    
# Displaying Variables
print("\nIntroduction:")
print("My name is", name)
print("My age is", age)
print("My height is", height)
print("My hobby is", hobby)

# Diplaying Variable Types
print("\nVariable Types:")
print(type(name))
print(type(age))
print(type(height))
print(type(hobby))
print(type(alive))
print(type(empty))

# Arithmetic Operators
print("\nArithmetic Operators:")
a = 20
b = 10
print("a is", a,)
print("b is", b)
print("a + b  =", a+b)
print("a - b  =", a-b)
print("a * b  =", a*b)
print("a / b  =", a/b)
print("a % b  =", a%b)
print("a ** b =", a**b)

# Relational Operators
print("\nRelational Operators:")
print("a is", a,)
print("b is", b)
print("a < b  =", a<b)
print("a <= b =", a<=b)
print("a == b =", a==b)
print("a >= b =", a>=b)
print("a > b  =", a>b)

# Assignment Operators
print("\nAssignment Operators")
print("a is", a)
a += 10
print("a after a += 10 is", a)
a -= 15
print("a after a -= 15 is", a)
a *= 10
print("a after a *= 10 is", a)
a /= 50
print("a after a /= 50 is", a)
a %= 5
print("a after a %= 5  is", a)
a **= 2
print("a after a **= 2 is", a)
# Logical Operators
print("\nLogical Operators:")
bool1 = True
bool2 = False
print("bool1 is",bool1)
print("bool2 is",bool2)
print("bool1 and bool2 =", bool1 and bool2)
print("bool1 or  bool2 =", bool1 or bool2)
print("not bool1 =", not bool1)
print("not bool2 =", not bool2)

# Multi Declaration
print("\nMulti Declaration:")
name,age,height = "Kaido",21,5.5
print("name,age,height = \"Kaido\",21,5.5")

# Type Casting
print("\nType Casting:")
num,string_num = 1,"2"
print("num,string_num = 1,\"2\"")
print("num + string_num = Error")
print("num + (int)string_num =", num+int(string_num))

# Taking Input
print("\nTaking Input:")
print("Every input is string if not type-casted")
name = input ("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
print(name, "is", age, "years old and", height, "tall")