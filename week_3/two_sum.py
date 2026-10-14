def two_sum(numbers: list, target: int = 9)-> list:
    seen = {}

    for index, number in enumerate(numbers):
        comp_number = target - number
        
        if comp_number in seen:
            return [seen[comp_number], index]
        
        seen[number] = index

    return []

numbers = [2, 7, 11, 15]
result = two_sum(numbers)
print(result)