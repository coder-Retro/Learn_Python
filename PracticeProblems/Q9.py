numbers = [1,2,3,4,5]

def reverse_list(lis):
    rev = []
    end = len(lis) - 1
    while end >= 0:
        rev.append(lis[end])
        end -= 1
    return rev

rev = reverse_list(numbers)
print(f"Original List: {numbers}")
print(f"Reversed List: {rev}")