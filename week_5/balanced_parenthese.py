def balanced_parenthese(words: str) -> str:
    count = 0

    for character in words:
        if character == "(":
            count += 1
        elif character == ")":
            count -= 1

    if count == 0:
        return "Output: Balanced"
    else:
        return "Output: Not Balanced"


user_input = "(a+b) * (c-d)"
# user_input = "(a+b))"
# user_input = "((a+b)"

result = balanced_parenthese(user_input)
print(result)