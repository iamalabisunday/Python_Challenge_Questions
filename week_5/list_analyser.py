def list_analyser(list_num: list) -> int:
    smallest = None
    largest = None
    total = 0
    average = None
    
    for num in list_num:
        if smallest is None or smallest > num:
            smallest = num
        elif largest is None or largest < num:
            largest = num
            
        total += num
        average = total / len(list_num)
        
    
    return f"Smallest Number: {smallest}, Largst number: {largest}, Total number: {total}, Average: {average}"

user_input = [12, 5, 27, 8, 14]
result = list_analyser(user_input)
print(result)
