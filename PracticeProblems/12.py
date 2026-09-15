maxOfTwo = lambda a,b: a if a>b else b

nums = [1,3,5,6,7,5,3,2,5]
first = True

for num in nums:
    if first:
        ans = num
        first = False
    ans = maxOfTwo(ans,num)

print(f"Maximum in {nums} is {ans}")