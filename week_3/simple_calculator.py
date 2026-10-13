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

while True:
    user_input = input("Input: ").lower()
    
    result = []
    if user_input == "undo":
        if len(result) < 2:
            print("Output: Nothing to undo")
            continue
        result.pop()
        print(result[-1])
        continue
        
    operator, number = user_input.split()
    if len(user_input) > 2:
        print("Output: Invaild input e.g + 5")
        continue
        
    if not "0" <= number <= "9":
        print("Output: Invaild Input e.g + 5")
        continue
    