def valid_number(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Error: enter a vaild number")


def number_reverser():
    user_input = valid_number("Input: ")

    number = abs(user_input)
    result = []

    while number > 0:
        rem = number % 10
        result.append(rem)
        number //= 10

    final_result = "".join(str(num) for num in result)

    if user_input < 0:
        final_result = "-" + final_result

    print(final_result)


number_reverser()
