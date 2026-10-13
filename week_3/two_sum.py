def two_sum(numbers: list, target: int = 9)-> list:
    for index, number in enumerate(numbers):
        comp_number = target - number
            
        if comp_number in numbers:
            comp_index = numbers.index(comp_number)
            
            if comp_index != index:
                return [index, comp_index]
    return []
    
numbers = [2, 7, 11, 15]
result = two_sum(numbers)
print(result)