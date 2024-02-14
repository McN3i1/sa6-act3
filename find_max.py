def find_max(numbers, compare_num):
    if not numbers:
        return ("List is empty")
    
    max = numbers[0]

    for num in numbers[1:]:
        max = compare_num(num, max)
    
    return max

list = [10, 2, 8, 4, 6]

greater = lambda x, y: x if x > y else y

result = find_max(list, greater)

print(result)