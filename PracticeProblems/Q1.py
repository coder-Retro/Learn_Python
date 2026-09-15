# Write a program to verify if a number is palindrome or not

def isPalindrome(x):
    copy = x
    rev = 0
    while (copy):
        rev = rev * 10 + copy % 10
        copy //= 10
    return rev == x

num = int(input("Enter a number: "))

print(f"{num} is a palindrome" if(isPalindrome(num)) else f"{num} is not a palindrome")