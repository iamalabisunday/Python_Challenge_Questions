
def number_reverser():
    user_input = int(input("Input: "))

    sign = -1 if user_input < 0 else 1
    number = abs(user_input)
    result = 0

    while number > 0:
        rem = number % 10
        result = result * 10 + rem
        number //= 10

    print(sign * result)


number_reverser()
