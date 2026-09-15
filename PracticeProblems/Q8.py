currSum = 0
first = True

while True:
    num = int(input("Enter a number: "))
    if num == -1:
        break
    if first:
        minSum = num
        maxSum = num
        first = False
    currSum += num
    maxSum = max(maxSum, num)
    minSum = min(minSum, num)

if not first:
    print(f"MaxSum: {maxSum}")
    print(f"MinSum: {minSum}")
else:
    print("No Numbers entered")