# Count the number of students with A grade in tuple
grade = ("C","D","A","A","B","B","A")
print("Grades :", grade)
print("Students with A grade :", grade.count("A"))

# Store the above values in a list and sort them fromt A to D
grad = list(grade).copy()
grad.sort()
print("Sorted Grades :", grad)