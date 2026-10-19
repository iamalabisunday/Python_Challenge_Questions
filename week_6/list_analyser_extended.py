numbers = [12, 5, 27, 8, 14, 27, 3]

def smallest_largest(numbers: list)-> int:
    smallest = float('inf')
    largest = float('-inf')
    
    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
            
    return f"Smallest: {smallest}\nLargest: {largest}"

def total(numbers: list[int])-> int:
    total = 0
    for number in numbers:
        total += number
    return total

def average(numbers: list[int]) -> float:
    sum_total = total(numbers)
    result = sum_total / len(numbers)
    return result

def number_above_avg(numbers: list[int])-> int:
    count = 0
    avg = average(numbers)
    for number in numbers:
        if number > avg:
            count += 1
    return count

print(smallest_largest(numbers))
print(f"Total: {total(numbers)}")
print(f"Average: {average(numbers):.2f}")
print(f"Numbers above average: {number_above_avg(numbers)}")

# Smallest: 3 (at index 6)
# Largest: 27 (at index 2)
# Total: 96
# Average: 13.71
# Numbers above average: 3
