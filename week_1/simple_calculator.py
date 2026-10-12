def calculator(first_numb: int, operator: str, second_numb:int) -> int:
    if operator == "+":
        return first_numb + second_numb
    elif operator == "-":
        return first_numb - second_numb
    elif operator == "*":
        return first_numb * second_numb
    elif operator == "/":
        if second_numb == 0:
            return "Output: Cannot divide by zero"
        return first_numb / second_numb
    else:
        return "Output: Invalid operator"
    
def input_numb(prompt: int) -> int:
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("Error: Kindly enter a vaild number")
        return input("Try again: ")

while True:
    first_num_input = input_numb("Enter the first number: ")
    operator_input = input("Enter your opetion (+, -, *, /): ").strip()
    second_num_input = input_numb("Enter the second number: ")
    
    result = calculator(first_num_input, operator_input, second_num_input)
    
    print(f"Answer: {result}")
    
    print("=" * 20)
    again = input("Do you want to try again: ").lower().strip()
    if again != "y":
        print("Goodbye!")
        break