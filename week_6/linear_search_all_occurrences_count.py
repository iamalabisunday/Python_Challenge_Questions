def found_index(values: list[int], target: int) -> list[int]:
    record = []
    count = 0
    for index, number in enumerate(values):
        if number == target:
            count += 1
            record.append(index)
        
    first = record[0]
    last = record[-1]
    
    if len(record) == 0:
        return "Target not found"
    
    return f"Found at index: {record} | Count: {count} | first: {first} | last: {last}"

values = [14, 7, 22, 9, 7, 31, 7, 5]

print(found_index(values, target=7)) 
print(found_index(values, target=22))
print(found_index(values, target=18))
