def duplicates(lists: list[int])-> int:
    record = {}
    for numb in lists:
        if numb in record:
            record[numb] += 1
        elif numb:
            record[numb] = 1
            
    lists = []
    for value, index in record.items():
        if index > 1:
            lists.append(value)
    
    if len(lists) == 0:
        return "no duplicates"
    else:
        return lists


# user_input = [1, 2, 3, 2, 4, 5, 1] # → [1, 2]
# user_input = [4, 4, 4, 4] # → [4]
# user_input = [1, 2, 3, 4] # → [] (no duplicates)
user_input = [10, 20, 10, 30, 20] # → [10, 20]

print(duplicates(user_input))