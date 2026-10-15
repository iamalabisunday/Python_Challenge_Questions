def is_letter(ch: str) -> bool:
    return "a" <= ch <= "z"


def is_palindrome(text: str) -> bool:
    left = 0
    right = len(text)-1

    while left < right:
        txt = text.lower()
        if not is_letter(txt[left]):
            left += 1
        if not is_letter(txt[right]):
            right -= 1
        if txt[left] != txt[right]:
            return "Output: Not a palindrome"
        left += 1
        right -= 1
    return "Output: Palindrome"


# user_input = is_palindrome("Was it a car or a cat I saw?")
# user_input = is_palindrome("Hello, World!")
# print(user_input)

user_input = input("Input: ").lower().strip()
result = is_palindrome(user_input)
print(result)
