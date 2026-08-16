# Check whether a lis in palindrome
lis = [1,2,3,2,1]
cop = lis.copy()
cop.reverse()

if cop == lis:
    print("list is palindrome")
else:
    print("list is not palindrome")