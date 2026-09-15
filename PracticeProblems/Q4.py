def avg(numbers):
    sum = 0
    count = 0
    for number in numbers:
        sum += number
        count += 1
    return sum / count

numbers = [1,2,3,4,5,6,7,8,9,10]
average = avg(numbers)
ans = list(filter(lambda x: x%2==0 and x>average,numbers))

print(f"Evens greater than avg of list: {ans}")