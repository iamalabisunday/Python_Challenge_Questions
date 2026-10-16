def second_largest(nums: list) -> int:
    
    largest_number = float('-inf')
    second_largest = float('-inf')
    
    for number in nums:
        if number > largest_number:
            largest_number = number
            
        if number < largest_number and second_largest != largest_number:
            second_largest = number
            
    return second_largest

numbers = [10, 5, 8, 20, 15]
result = second_largest(numbers)
print("Output:", result)

# Input: [10, 5, 8, 20, 15] → Output: 15
# Input: [4, 9, 2, 9, 7] → Output: 7