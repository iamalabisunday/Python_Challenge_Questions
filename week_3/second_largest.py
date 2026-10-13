def second_largest(user_list : list) -> int:
    first_largest = None
    second_largest = None
    
    for num in user_list:
        try:
            number = int(num)
            if first_largest is None or (number > first_largest):
                second_largest = first_largest
                first_largest = number
            
            if second_largest is None or (number > second_largest and number != first_largest):
                second_largest = number
        except ValueError:
            return "Output: Invaild number"
            
    return f"Output: {second_largest}"


user_list = input("Input: ").strip().split(",")
result = second_largest(user_list)
print(result)