def is_letter(chr) -> bool:
    return "a" <= chr <= "z" or "A" <= chr <= "Z"

def is_palindrome(text, left=0, right=None) -> str:
    text = text.lower()

    if right is None:
        right = len(text)-1

    if not is_letter(text[left]):
        return is_palindrome(text, left + 1, right)

    if not is_letter(text[right]):
        return is_palindrome(text, left, right - 1)

    if text[left] == text[right]:
        return "Output: Palindrome"

    if text[left] != text[right]:
        return "Output: Not a palindrome"

    return is_palindrome(text, left + 1, right - 1)

input_1 = "Was it a car or a cat I saw?"
input_2 = "Hello, World!"

result = is_palindrome(input_2)
print(result)