# Write a program to print fizz buss on numbers from 1 to 30 using divisibility test

def classify(n):
    if (n%3==0 and n%5==0):
        return "FizzBuzz"
    elif (n%3==0):
        return "Fizz"
    elif (n%5==0):
        return "Buzz"
    else:
        return n

for i in range(1,31):
    print(classify(i))