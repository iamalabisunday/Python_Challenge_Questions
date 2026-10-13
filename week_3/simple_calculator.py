def calculator(first_numb: int, operator: str, second_numb: int):
    if operator == "+":
        return first_numb + second_numb
    elif operator == "-":
        return first_numb - second_numb
    elif operator == "*":
        return first_numb * second_numb
    elif operator == "/":
        if second_numb == 0:
            return "Output: Cannot be divided by zero"
        return first_numb / second_numb
    else:
        return "Output:  Error: Invaild Operator"

list_of_result = []
sum_total = 0
    
while True:
    user_input = input("Input: ").lower()
    
    if user_input == "undo":
        if len(list_of_result) < 2:
            print("Output: Nothing to undo")
            continue
        list_of_result.pop()
        print(f"Output: {list_of_result[-1]}")
        sum_total = sum_total - list_of_result[-1]
        continue
    
    try:
        operator, number = user_input.split()
        numb = int(number)
        result = calculator(sum_total, operator, numb)
        if isinstance(result, int):
            sum_total = result
            list_of_result.append(sum_total)
            print(f"Output: {sum_total}")
        else:
            print(result)
    except ValueError:
        print("Output: Invaild number input e.g + 5")